"""Testes de rotas, autenticação e saúde."""

import unittest

from app import create_app
from app.extensions import db
from app.models import Usuario
from app.security import conferir_senha, gerar_hash, senha_forte

SENHA_DEMO = "flask2026"  # noqa: S105


class FlaskSmokeTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            db.session.add(Usuario(nome_usuario="joao", senha_hash=gerar_hash(SENHA_DEMO)))
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def _login(self, usuario="joao", senha=SENHA_DEMO):
        return self.client.post(
            "/autenticar",
            data={"nome_usuario": usuario, "senha": senha},
        )

    # --- páginas -----------------------------------------------------------
    def test_paginas_principais(self):
        for rota in ["/", "/index", "/ola", "/contato", "/login", "/health"]:
            with self.subTest(rota=rota):
                self.assertEqual(self.client.get(rota).status_code, 200)

    def test_rota_com_parametros(self):
        resposta = self.client.get("/ola/Joao")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b"Joao", resposta.data)

        self._login()
        resposta = self.client.get("/usuario/Ana/Estudante/Python")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b"Ana", resposta.data)
        self.assertIn(b"Python", resposta.data)

    def test_novo_cadastro(self):
        resposta = self.client.post("/novocadastro/", data={"nome_usuario": "novo_aluno"})
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b"novo_aluno", resposta.data)

    # --- autenticação ------------------------------------------------------
    def test_login_valido(self):
        resposta = self._login()
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b"Acesso permitido", resposta.data)

        with self.client.session_transaction() as sessao:
            self.assertEqual(sessao.get("usuario"), "joao")

    def test_login_invalido_redireciona(self):
        resposta = self._login(senha="errada")
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(resposta.headers["Location"], "/login")

    def test_login_por_get_nao_aceito(self):
        resposta = self.client.get(f"/autenticar?nome_usuario=joao&senha={SENHA_DEMO}")
        self.assertEqual(resposta.status_code, 405)

    def test_usuario_exige_login(self):
        self.assertEqual(self.client.get("/usuario").status_code, 302)
        self._login()
        self.assertEqual(self.client.get("/usuario").status_code, 200)

    def test_logout_limpa_sessao(self):
        self._login()
        with self.client.session_transaction() as sessao:
            self.assertIn("usuario", sessao)

        resposta = self.client.post("/logout")
        self.assertEqual(resposta.status_code, 302)

        with self.client.session_transaction() as sessao:
            self.assertNotIn("usuario", sessao)

    # --- segurança ---------------------------------------------------------
    def test_senha_armazenada_como_hash(self):
        with self.app.app_context():
            usuario = db.session.scalar(db.select(Usuario).where(Usuario.nome_usuario == "joao"))
            self.assertNotEqual(usuario.senha_hash, SENHA_DEMO)
            self.assertTrue(conferir_senha(usuario.senha_hash, SENHA_DEMO))
            self.assertFalse(conferir_senha(usuario.senha_hash, "outra"))

    def test_politica_de_senha(self):
        self.assertFalse(senha_forte("curta1"))
        self.assertFalse(senha_forte("12345678"))
        self.assertTrue(senha_forte("senha123"))

    # --- infraestrutura ----------------------------------------------------
    def test_health(self):
        resposta = self.client.get("/health")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json(), {"status": "ok"})

    def test_ready(self):
        resposta = self.client.get("/ready")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json(), {"status": "ready"})

    def test_404_em_json(self):
        resposta = self.client.get("/rota-inexistente")
        self.assertEqual(resposta.status_code, 404)
        self.assertEqual(resposta.get_json(), {"erro": "nao encontrado"})


if __name__ == "__main__":
    unittest.main()
