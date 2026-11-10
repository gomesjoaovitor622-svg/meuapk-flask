"""Autenticação.

Fase 2: refatoração pura — a tabela em memória e a comparação de senha em
texto puro serão substituídas por banco + hash na Fase 3.
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for

bp = Blueprint("auth", __name__)

tabela_usuarios = {
    "joao": "flask2026",
    "alunoIFRO": "flask2026",
    "visitante": "flask2026",
}


def verificar_login(login: str, senha: str) -> bool:
    return tabela_usuarios.get(login) == senha


@bp.get("/login")
def login():
    return render_template("t_login.html")


@bp.route("/autenticar", methods=["GET", "POST"])
def autenticar():
    if request.method == "POST":
        usuario = request.form.get("nome_usuario")
        senha = request.form.get("senha")
    else:
        usuario = request.args.get("nome_usuario")
        senha = request.args.get("senha")

    if verificar_login(usuario, senha):
        return render_template("t_sucesso.html", usuario=usuario)

    flash("Login ou senha inválidos!")
    return redirect(url_for("auth.login"))
