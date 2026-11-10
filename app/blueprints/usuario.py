"""Rotas de perfil e cadastro (protegidas por sessão)."""

from flask import Blueprint, render_template, request

from ..security import login_obrigatorio

bp = Blueprint("usuario", __name__)


@bp.get("/usuario")
@login_obrigatorio
def dados_usuario():
    dados_usu = {"profissao": "Estudante", "disciplina": "Desenvolvimento Web III"}
    return render_template("t_usuario.html", nome="Joao Vitor", dados=dados_usu)


@bp.get("/usuario/<p_nome>/<p_profissao>/<p_disciplina>")
@login_obrigatorio
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usu = {"profissao": p_profissao, "disciplina": p_disciplina}
    return render_template("t_usuario.html", nome=p_nome, dados=dados_usu)


@bp.post("/novocadastro/")
def cadastro_usuario():
    nome_usuario = request.form.get("nome_usuario", "")
    return render_template("t_cadastro.html", nome_login=nome_usuario)
