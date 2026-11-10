"""Configuração da aplicação por ambiente.

Nenhum segredo vive no código: tudo vem de variáveis de ambiente
(carregadas de `.env` em desenvolvimento).
"""

import os
from datetime import timedelta

from dotenv import load_dotenv

# Carrega `.env` antes de ler qualquer variável de ambiente.
load_dotenv()


def _bool(nome: str, padrao: bool = False) -> bool:
    return os.getenv(nome, str(padrao)).strip().lower() in {"1", "true", "sim", "yes"}


def _int(nome: str, padrao: int) -> int:
    valor = os.getenv(nome)
    if valor is None or not valor.strip():
        return padrao
    return int(valor)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///meuapk.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = _bool("SESSION_COOKIE_SECURE", False)
    PERMANENT_SESSION_LIFETIME = timedelta(hours=_int("SESSION_HORAS", 8))
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SAMESITE = "Lax"

    MAX_CONTENT_LENGTH = _int("MAX_CONTENT_LENGTH", 1 * 1024 * 1024)

    RATELIMIT_STORAGE_URI = os.getenv("RATELIMIT_STORAGE_URI", "memory://")
    RATELIMIT_HEADERS_ENABLED = True

    WTF_CSRF_TIME_LIMIT = None


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = "chave-de-teste-nao-use-em-producao"  # noqa: S105
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    RATELIMIT_ENABLED = False


class ProdConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True


CONFIGS = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
}
