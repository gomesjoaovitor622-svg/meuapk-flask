"""Rotas institucionais: início, saudação e contato."""

from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.get("/")
@bp.get("/index")
def index():
    return render_template("t_index.html", nome="Turma 2026")


@bp.get("/ola")
def raiz():
    return render_template("t_index.html", nome="Turma 2026")


@bp.get("/ola/<id>")
def saudacao(id):
    return render_template("t_index.html", nome=id)


@bp.get("/contato")
def contato():
    return render_template("t_contato.html")
