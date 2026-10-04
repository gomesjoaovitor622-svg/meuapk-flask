import unittest

from app import meu_site, verificar_login


class FlaskSmokeTests(unittest.TestCase):
    def setUp(self):
        self.client = meu_site.test_client()

    def test_paginas_principais(self):
        for rota in ['/', '/index', '/ola', '/contato', '/usuario', '/login']:
            with self.subTest(rota=rota):
                resposta = self.client.get(rota)
                self.assertEqual(resposta.status_code, 200)

    def test_rota_com_parametros(self):
        resposta = self.client.get('/ola/Joao')
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b'Joao', resposta.data)

        resposta = self.client.get('/usuario/Ana/Estudante/Python')
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b'Ana', resposta.data)
        self.assertIn(b'Python', resposta.data)

    def test_login_valido(self):
        resposta = self.client.post(
            '/autenticar',
            data={'nome_usuario': 'joao', 'senha': 'flask2026'},
        )
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b'Acesso permitido', resposta.data)

    def test_login_invalido_redireciona(self):
        resposta = self.client.post(
            '/autenticar',
            data={'nome_usuario': 'joao', 'senha': 'errada'},
            follow_redirects=False,
        )
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(resposta.headers['Location'], '/login')

    def test_novo_cadastro(self):
        resposta = self.client.post(
            '/novocadastro/',
            data={'nome_usuario': 'novo_aluno'},
        )
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b'novo_aluno', resposta.data)

    def test_funcao_login(self):
        self.assertTrue(verificar_login('joao', 'flask2026'))
        self.assertFalse(verificar_login('joao', 'senha_errada'))
        self.assertFalse(verificar_login('nao_existe', 'flask2026'))


if __name__ == '__main__':
    unittest.main()
