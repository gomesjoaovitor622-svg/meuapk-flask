# Evidências de teste — Atividade GitHub + Flask

## Base utilizada
O projeto foi reconstruído a partir do arquivo-base fornecido na aula, consolidando `appFlask_v1.py` até `appFlask_v8.py` em um único `app.py`. A sequência dos commits preserva essa evolução.

## Testes executados neste ambiente

### 1. Sintaxe Python
`python -m py_compile app.py` → **OK**.

### 2. Templates Jinja2
Todos os templates de `t_templates/` foram carregados pelo Jinja2 sem erro de sintaxe:
- `base.html`
- `t_cadastro.html`
- `t_contato.html`
- `t_index.html`
- `t_login.html`
- `t_usuario.html`

### 3. Rotas
Foram verificadas as rotas e métodos esperados:
- `/`
- `/index`
- `/ola`
- `/ola/<id>`
- `/contato`
- `/usuario`
- `/usuario/<p_nome>/<p_profissao>/<p_disciplina>`
- `/login`
- `/autenticar` — GET e POST
- `/novocadastro/` — POST

Resultado: **OK**.

### 4. Lógica de autenticação
- Login válido `joao / flask2026` → acesso permitido.
- Login inválido → redirecionamento para `/login` e mensagem `flash`.
- Novo cadastro → renderização de `t_cadastro.html`.

Resultado: **OK**.

### 5. Arquivos estáticos
As referências do template foram auditadas e os arquivos referenciados existem:
- `static/css/estilo.css`
- `static/img/logo.svg`
- `static/img/professora.svg`

Resultado: **OK**.

### 6. Git
- `main` e `aula6-heranca` existem.
- A evolução possui commits separados para as versões 1 a 8.
- A branch de herança possui commits próprios e foi integrada à `main`.
- O projeto possui somente **um arquivo Python principal: `app.py`**.
- `venv/`, `.venv/`, `__pycache__/` e `*.pyc` estão ignorados.

## Limitação do ambiente
O ambiente usado para preparar o arquivo não possui Flask instalado e está sem acesso de rede para instalar a dependência. Por isso, não foi possível executar um servidor Flask real nem produzir prints HTTP autênticos aqui. A sintaxe, os templates, o mapeamento das rotas e a lógica das funções foram testados sem inventar resultados de navegador.

## Teste final no computador
```bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Depois, abra `http://127.0.0.1:7000` e faça as capturas solicitadas pela atividade.
