# Arquitetura

## Visão geral

Aplicação Flask server-rendered, organizada em camadas finas:

```
Requisição HTTP
      │
      ▼
app/__init__.py        create_app(): lê o ambiente, registra extensões e blueprints
      │
      ├── app/config.py        Config / DevConfig / TestConfig / ProdConfig
      ├── app/extensions.py    db, migrate, csrf, limiter
      ├── app/models.py        Usuario
      ├── app/security.py      hash de senha, política, login_obrigatorio
      │
      └── app/blueprints/
            ├── main.py        /, /index, /ola, /ola/<id>, /contato
            ├── auth.py        /login, /autenticar, /logout
            ├── usuario.py     /usuario, /usuario/<...>, /novocadastro/
            └── health.py      /health, /ready
```

## Fluxo de uma requisição autenticada

1. `create_app()` carrega a configuração do ambiente (`FLASK_ENV`).
2. O blueprint recebe a rota.
3. Se a rota usa `@login_obrigatorio`, a sessão é verificada; sem sessão o
   usuário é redirecionado para `/login`.
4. O template Jinja2 é renderizado sobre `base.html`.

## Fluxo de login

1. `GET /login` renderiza o formulário com um token CSRF.
2. `POST /autenticar` valida o token CSRF, aplica rate limit de 5/min e busca
   o usuário no banco.
3. A senha é conferida com `scrypt` contra `Usuario.senha_hash`.
4. Em caso de sucesso, a sessão é recriada (`session.clear()` antes de gravar,
   evitando fixação de sessão) e o usuário é gravado em `session["usuario"]`.

## Ambientes

| Ambiente | Uso | Banco | CSRF | Rate limit | Cookie Secure |
|---|---|---|---|---|---|
| `dev` | local | sqlite | on | on | off |
| `test` | pytest | sqlite em memória | off | off | off |
| `prod` | container | `/data/meuapk.db` | on | on | on |

## Deploy

- `deploy/Dockerfile`: imagem `python:3.12-slim`, usuário `appuser` (uid 10001),
  healthcheck em `/health`, `gunicorn` com 2 workers.
- `deploy/entrypoint.sh`: roda `flask db upgrade` antes de iniciar o servidor.
- `deploy/docker-compose.yml`: volume para o banco, `read_only`, `cap_drop: ALL`,
  `no-new-privileges`.

## Decisões

- **Sessão em cookie, não JWT**: a aplicação é server-rendered; sessão assinada
  com `SECRET_KEY` é mais simples e permite logout real.
- **Flask-Migrate/Alembic**: migrações versionadas em vez de `create_all()` em
  produção.
- **Seed por ambiente**: nenhuma senha padrão no código; `scripts/seed.py` lê
  `ADMIN_SENHA`, `ALUNO_SENHA` e `VISITANTE_SENHA`.
