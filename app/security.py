"""Primitivas de segurança: hash de senha e controle de sessão."""

from functools import wraps

from flask import redirect, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

METODO_HASH = "scrypt"
TAMANHO_MINIMO_SENHA = 8


def gerar_hash(senha: str) -> str:
    """Gera hash de senha com scrypt (padrão do Werkzeug)."""
    return generate_password_hash(senha, method=METODO_HASH)


def conferir_senha(hash_armazenado: str, senha: str) -> bool:
    """Confere a senha em tempo constante contra o hash armazenado."""
    return check_password_hash(hash_armazenado, senha)


def senha_forte(senha: str) -> bool:
    """Política mínima: 8+ caracteres, com letra e número."""
    return (
        len(senha) >= TAMANHO_MINIMO_SENHA
        and any(c.isalpha() for c in senha)
        and any(c.isdigit() for c in senha)
    )


def login_obrigatorio(view):
    """Redireciona para o login quando não há sessão ativa."""

    @wraps(view)
    def wrapper(*args, **kwargs):
        if not session.get("usuario"):
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapper
