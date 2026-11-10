"""Autenticação: login por POST, sessão e logout."""

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from ..extensions import db, limiter
from ..models import Usuario
from ..security import conferir_senha

bp = Blueprint("auth", __name__)

MENSAGEM_CREDENCIAL_INVALIDA = "Login ou senha inválidos!"


@bp.get("/login")
def login():
    return render_template("t_login.html")


@bp.post("/autenticar")
@limiter.limit("5 per minute")
def autenticar():
    usuario = (request.form.get("nome_usuario") or "").strip()
    senha = request.form.get("senha") or ""

    registro = db.session.scalar(
        db.select(Usuario).where(Usuario.nome_usuario == usuario, Usuario.ativo.is_(True))
    )

    if registro is not None and conferir_senha(registro.senha_hash, senha):
        session.clear()
        session["usuario"] = registro.nome_usuario
        session.permanent = True
        return render_template("t_sucesso.html", usuario=registro.nome_usuario)

    flash(MENSAGEM_CREDENCIAL_INVALIDA)
    return redirect(url_for("auth.login"))


@bp.post("/logout")
def logout():
    session.clear()
    flash("Sessão encerrada.")
    return redirect(url_for("main.index"))
