"""Modelos de dados."""

from datetime import UTC, datetime

from .extensions import db


def _agora() -> datetime:
    return datetime.now(UTC)


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(64), unique=True, nullable=False, index=True)
    senha_hash = db.Column(db.String(255), nullable=False)
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    criado_em = db.Column(db.DateTime, default=_agora, nullable=False)

    def __repr__(self) -> str:  # pragma: no cover - conveniência de debug
        return f"<Usuario {self.nome_usuario!r}>"
