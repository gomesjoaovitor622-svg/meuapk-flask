# FlaskLab — Desenvolvimento Web III

Aplicação Flask com autenticação, construída a partir do código-base da aula e
evoluída para uma estrutura de projeto real: app factory, blueprints,
configuração por ambiente, banco de dados, testes, Docker e CI.

## Stack

- Python 3.11+ / Flask 3
- SQLAlchemy + Flask-Migrate (Alembic)
- Flask-WTF (CSRF) e Flask-Limiter (rate limit)
- Gunicorn + Docker
- pytest, ruff, pip-audit, detect-secrets

## Estrutura

```
app/
├── __init__.py          # create_app()
├── config.py            # Dev / Test / Prod
├── extensions.py        # db, migrate, csrf, limiter
├── models.py            # Usuario
├── security.py          # hash de senha, política, login_obrigatorio
├── blueprints/          # main, auth, usuario, health
├── templates/           # Jinja2 (base + páginas)
└── static/              # CSS, JS e imagens
migrations/              # migrações Alembic
scripts/seed.py          # usuários de demonstração
tests/                   # suíte pytest
deploy/                  # Dockerfile, compose e entrypoint
docs/                    # arquitetura e documentação
docs/legado/templates/   # templates das primeiras versões (histórico)
```

## Como executar

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS

pip install -r requirements-dev.txt

copy .env.example .env         # Windows
# cp .env.example .env         # Linux/macOS
```

Edite o `.env` e gere uma `SECRET_KEY`:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Depois:

```bash
flask --app wsgi db upgrade
python -m scripts.seed
python run.py
```

Abra `http://127.0.0.1:7000`.

### Usuários de demonstração

Criados por `scripts/seed.py` a partir do `.env` — **nenhuma senha fica no
código**. Defina antes de rodar o seed:

```env
ADMIN_USUARIO=joao
ADMIN_SENHA=defina-uma-senha-forte
ALUNO_SENHA=defina-uma-senha-forte
VISITANTE_SENHA=defina-uma-senha-forte
```

## Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/`, `/index` | Página inicial |
| GET | `/ola`, `/ola/<id>` | Saudação |
| GET | `/contato` | Contato |
| GET | `/login` | Formulário de login |
| POST | `/autenticar` | Autentica (só POST; CSRF + rate limit) |
| POST | `/logout` | Encerra a sessão |
| GET | `/usuario` | Perfil (exige login) |
| GET | `/usuario/<nome>/<profissao>/<disciplina>` | Perfil parametrizado (exige login) |
| POST | `/novocadastro/` | Cadastro |
| GET | `/health` | Liveness |
| GET | `/ready` | Readiness (testa o banco) |

## Testes e qualidade

```bash
pytest                      # testes + cobertura (mínimo 70%)
ruff check .                # lint
ruff format --check .       # formatação
```

## Docker

```bash
docker compose -f deploy/docker-compose.yml up --build
```

A aplicação sobe em `http://127.0.0.1:8000`, com migrações aplicadas no
entrypoint, usuário não-root, `cap_drop: ALL` e filesystem read-only.

## Segurança

- Senhas com `scrypt`; nunca em texto puro.
- Login apenas por `POST`, com proteção CSRF.
- Sessão `HttpOnly` + `SameSite=Lax` (`Secure` em produção).
- Rate limit de 5 tentativas/minuto no login.
- `SECRET_KEY` obrigatória, vinda do ambiente.
- Dependências fixadas com hash e auditadas no CI.

Detalhes em [SECURITY.md](SECURITY.md) e [docs/ARQUITETURA.md](docs/ARQUITETURA.md).

## Histórico

O repositório preserva a evolução da atividade (`appFlask_v1` … `v8`) no
histórico Git. A branch `aula6-heranca` contém a introdução de `base.html` e
herança de templates. Os templates das primeiras versões foram movidos para
`docs/legado/templates/`.

## Licença

MIT — veja [LICENSE](LICENSE).
