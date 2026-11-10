"""App factory do meuapk-flask."""

import os

from flask import Flask, jsonify
from flask_wtf.csrf import CSRFError

from .config import CONFIGS
from .extensions import csrf, db, limiter, migrate


def create_app(config_name: str | None = None) -> Flask:
    """Cria a aplicação Flask para o ambiente informado.

    O ambiente pode vir do argumento ou de FLASK_ENV (dev por padrão).
    """
    app = Flask(__name__)

    nome = config_name or os.getenv("FLASK_ENV", "dev")
    if nome not in CONFIGS:
        raise RuntimeError(f"FLASK_ENV invalido: {nome!r}. Use um destes: {', '.join(CONFIGS)}")
    app.config.from_object(CONFIGS[nome])

    if not app.config.get("SECRET_KEY"):
        raise RuntimeError(
            "SECRET_KEY nao definida. Copie .env.example para .env e defina "
            'uma chave com: python -c "import secrets; print(secrets.token_hex(32))"'
        )

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    limiter.init_app(app)

    from .blueprints.auth import bp as auth_bp
    from .blueprints.health import bp as health_bp
    from .blueprints.main import bp as main_bp
    from .blueprints.usuario import bp as usuario_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(health_bp)

    @app.errorhandler(404)
    def nao_encontrado(_erro):
        return jsonify(erro="nao encontrado"), 404

    @app.errorhandler(500)
    def erro_interno(_erro):
        return jsonify(erro="erro interno"), 500

    @app.errorhandler(CSRFError)
    def csrf_invalido(erro):
        return jsonify(erro="requisicao invalida", motivo=erro.description), 400

    return app
