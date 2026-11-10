"""Cria os usuários de demonstração.

As senhas vêm de variáveis de ambiente (ADMIN_SENHA, ALUNO_SENHA,
VISITANTE_SENHA). Usuários sem senha definida são ignorados.

Uso:
    python -m scripts.seed
"""

import os

from app import create_app
from app.extensions import db
from app.models import Usuario
from app.security import gerar_hash


def executar() -> None:
    app = create_app()
    with app.app_context():
        db.create_all()

        usuarios = [
            (os.getenv("ADMIN_USUARIO", "joao"), os.getenv("ADMIN_SENHA")),
            ("alunoIFRO", os.getenv("ALUNO_SENHA")),
            ("visitante", os.getenv("VISITANTE_SENHA")),
        ]

        criados = 0
        for nome, senha in usuarios:
            if not nome or not senha:
                continue
            existe = db.session.scalar(db.select(Usuario).where(Usuario.nome_usuario == nome))
            if existe is None:
                db.session.add(Usuario(nome_usuario=nome, senha_hash=gerar_hash(senha)))
                criados += 1

        db.session.commit()
        print(f"Seed concluído: {criados} usuário(s) criado(s).")


if __name__ == "__main__":
    executar()
