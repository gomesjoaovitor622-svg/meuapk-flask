"""Endpoints de saúde para Docker, proxy e monitoramento."""

from flask import Blueprint, jsonify
from sqlalchemy import text

from ..extensions import db

bp = Blueprint("health", __name__)


@bp.get("/health")
def health():
    return jsonify(status="ok"), 200


@bp.get("/ready")
def ready():
    try:
        db.session.execute(text("SELECT 1"))
    except Exception:  # noqa: BLE001
        return jsonify(status="unavailable"), 503
    return jsonify(status="ready"), 200
