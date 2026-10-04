# Evidências de teste — Atividade GitHub + Flask

## 1. Base utilizada
O projeto foi revisado a partir do código-base fornecido na aula, que contém `appFlask_v1.py` até `appFlask_v8.py`. A implementação final consolida essa evolução em um único `app.py`, mantendo o histórico no Git por commits e branch.

## 2. Revisão realizada
Foram revisados:
- código Python (`app.py`);
- todas as rotas e métodos HTTP;
- templates Jinja2 em `t_templates/`;
- arquivos CSS, JavaScript e imagens;
- referências `url_for()` dos templates;
- fluxo de login, `flash`, `redirect` e cadastro;
- `requirements.txt` e `.gitignore`;
- histórico, branches e integridade do repositório Git.

Durante a revisão foi encontrado e corrigido um problema importante: a rota `/novocadastro/` estava declarada depois do `app.run()`. Isso poderia impedir o registro dessa rota quando o servidor fosse iniciado diretamente com `python app.py`. A rota foi movida para antes do bloco `if __name__ == '__main__':`.

Também foi restaurado no login o botão **Novo Cadastro**, usando o formulário POST da versão 8 da base da aula.

## 3. Testes executados

### 3.1 Sintaxe Python
Comando:
```text
python -m py_compile app.py test_smoke.py
```
Resultado: **OK**.

### 3.2 Templates Jinja2
Todos os templates abaixo foram carregados e renderizados com Jinja2, usando contextos representativos:
- `base.html`
- `t_index.html`
- `t_contato.html`
- `t_usuario.html`
- `t_login.html`
- `t_cadastro.html`

Resultado registrado: **JINJA_RENDER_OK**.

### 3.3 Arquivos estáticos
Foram verificadas as referências utilizadas pelos templates:
- `static/css/estilo.css`
- `static/img/logo.svg`
- `static/img/professora.svg`

Resultado registrado: **ASSETS_OK**.

### 3.4 Rotas
A estrutura das rotas foi analisada automaticamente pelo AST do Python. Foram confirmadas:
- `/` — GET
- `/index` — GET
- `/ola` — GET
- `/ola/<id>` — GET
- `/contato` — GET
- `/usuario` — GET
- `/usuario/<p_nome>/<p_profissao>/<p_disciplina>` — GET
- `/login` — GET
- `/autenticar` — GET e POST
- `/novocadastro/` — POST

Também foi confirmado que o `app.run()` está depois de todas as declarações de rotas.

Resultado: **RUN_AFTER_ROUTES True**.

### 3.5 Lógica das funções e rotas
Foi executado um teste de lógica com um stub temporário do Flask, sem alterar o projeto, verificando:
- registro das 10 rotas;
- métodos HTTP de cada rota;
- login válido;
- login inválido;
- redirecionamento para `/login`;
- mensagem `flash` de erro;
- cadastro de usuário;
- parâmetros de rotas;
- função `verificar_login()`.

Resultado real do teste:
```text
ALL_LOGIC_TESTS_OK
```

**Importante:** esse teste verifica a lógica e o mapeamento das funções sem executar o framework Flask real.

### 3.6 Teste automatizado para Flask real
Foi incluído `test_smoke.py`, que utiliza o `test_client()` oficial do Flask para testar:
- páginas principais;
- rotas com parâmetros;
- login válido;
- login inválido e HTTP 302;
- cadastro;
- `verificar_login()`.

O teste está pronto para ser executado no computador com:
```text
pip install -r requirements.txt
python -m unittest -v test_smoke.py
```

No ambiente desta preparação, o pacote Flask não está instalado e não há acesso de rede para instalar a dependência. Por isso, **não foi inventado um resultado de execução do Flask real**.

### 3.7 Git
Foram confirmados:
- branch `main`;
- branch `aula6-heranca`;
- commits correspondentes às versões 1 a 8;
- merge da branch de herança;
- working tree sem alterações após o commit final;
- integridade do repositório com `git fsck --full` sem erros;
- `.gitignore` contendo `venv/`, `.venv/`, `__pycache__/`, `*.pyc`, `.env` e `.vscode/`.

## 4. Resultado da revisão
**Código revisado e corrigido.** Os testes possíveis neste ambiente foram executados. O único teste que não pôde ser executado aqui é o teste HTTP com o Flask real, porque a dependência não está instalada e o ambiente não possui acesso à Internet para instalá-la.

## 5. Teste final no computador
No Windows/VS Code:
```text
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m unittest -v test_smoke.py
python app.py
```

Depois acessar:
```text
http://127.0.0.1:7000
```

Login de teste:
```text
Usuário: joao
Senha: flask2026
```

Também estão disponíveis `alunoIFRO` e `visitante`, ambos com a senha `flask2026`.
