from flask import Flask

meu_site = Flask(__name__)


@meu_site.route('/')
@meu_site.route('/ola')
def raiz():
    return 'Olá, Turma 2026!'


@meu_site.route('/contato')
def contato():
    return 'e-mail: joaovitor@ifro.edu.br'


@meu_site.route('/rota2')
def rota2():
    resposta = '<H3>Olá, Turma 2026!</H3>'
    resposta += '<H4>Sou a rota 2</H4>'
    return resposta


def saudacoes(nome):
    return f'Boa noite, {nome}! Tudo bem?'


if __name__ == '__main__':
    meu_site.run(port=7000)
