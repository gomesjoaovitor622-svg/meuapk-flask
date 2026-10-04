from flask import Flask, render_template

meu_site = Flask(__name__)


@meu_site.route('/')
@meu_site.route('/ola')
def raiz():
    return render_template('homepage.html')


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


def saudacoes(nome):
    return f'Boa noite, {nome}! Tudo bem?'


if __name__ == '__main__':
    meu_site.run(port=7000)
