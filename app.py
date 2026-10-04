from flask import Flask, render_template, request, flash, redirect

meu_site = Flask(__name__, template_folder='t_templates')
meu_site.config['SECRET_KEY'] = 'atividade-flask-joao-vitor'


@meu_site.route('/ola')
def raiz():
    return render_template('t_index.html', nome='Turma 2026')


@meu_site.route('/ola/<id>')
def saudacao(id):
    return render_template('t_index.html', nome=id)


@meu_site.route('/')
@meu_site.route('/index')
def index():
    return render_template('t_index.html', nome='Turma 2026')


@meu_site.route('/contato')
def contato():
    return render_template('t_contato.html')


@meu_site.route('/login')
def login():
    return render_template('t_login.html')


tabelaUsuarios = {
    'joao': 'flask2026',
    'alunoIFRO': 'flask2026',
    'visitante': 'flask2026',
}


def verificar_login(login, senha):
    return login in tabelaUsuarios and tabelaUsuarios[login] == senha


@meu_site.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    usuario = request.form.get('nome_usuario') if request.method == 'POST' else request.args.get('nome_usuario')
    senha = request.form.get('senha') if request.method == 'POST' else request.args.get('senha')
    if verificar_login(usuario, senha):
        return f'Login e senha corretos. Acesso permitido para {usuario}!'
    flash('Login ou senha inválidos!')
    return redirect('/login')


@meu_site.route('/usuario')
def dados_usuario():
    dados_usu = {'profissao': 'Estudante', 'disciplina': 'Desenvolvimento Web III'}
    return render_template('t_usuario.html', nome='Joao Vitor', dados=dados_usu)


@meu_site.route('/usuario/<p_nome>/<p_profissao>/<p_disciplina>')
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usu = {'profissao': p_profissao, 'disciplina': p_disciplina}
    return render_template('t_usuario.html', nome=p_nome, dados=dados_usu)


def saudacoes(nome):
    return f'Boa noite, {nome}! Tudo bem?'



@meu_site.route('/novocadastro/', methods=['POST'])
def cadastro_usuario():
    nome_usuario = request.form.get('nome_usuario', '')
    return render_template('t_cadastro.html', nome_login=nome_usuario)


if __name__ == '__main__':
    meu_site.run(port=7000)
