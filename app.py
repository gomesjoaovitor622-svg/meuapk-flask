from flask import Flask, render_template

meu_site = Flask(__name__)


@meu_site.route('/')
@meu_site.route('/ola')
def raiz():
    return render_template('homepage.html')


@meu_site.route('/ola/<id>')
def saudacao(id):
    return render_template('homepage_nome.html', campoNome=id)


@meu_site.route('/index')
def index():
    return render_template('index.html')


@meu_site.route('/contato')
def contato():
    return render_template('contato.html')


@meu_site.route('/usuario')
def dados_usuario():
    dados_usu = {
        'nome': 'Joao Vitor',
        'profissao': 'Estudante',
        'disciplina': 'Desenvolvimento Web III',
    }
    return render_template('usuario.html', dados=dados_usu)


@meu_site.route('/usuario/<p_nome>/<p_profissao>/<p_disciplina>')
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usu = {'nome': p_nome, 'profissao': p_profissao, 'disciplina': p_disciplina}
    return render_template('usuario.html', dados=dados_usu)


def saudacoes(nome):
    return f'Boa noite, {nome}! Tudo bem?'


if __name__ == '__main__':
    meu_site.run(port=7000)
