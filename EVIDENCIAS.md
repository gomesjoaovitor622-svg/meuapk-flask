# Evidências de teste

## Verificações realizadas no ambiente de preparação
- Sintaxe de `app.py` validada com `python -m py_compile app.py`.
- Histórico Git validado com `git log --oneline --decorate --graph --all`.
- Branch `main` e branch `aula6-heranca` criadas.
- `app.py` permanece como único arquivo Python principal do projeto.
- `venv/`, `.venv/`, `__pycache__/` e `.pyc` estão no `.gitignore`.
- Templates com herança usam `base.html`, `{% extends %}` e `{% block conteudo %}`.

## Testes para executar no computador
Depois de `pip install -r requirements.txt` e `python app.py`, verificar:
1. `/` — página inicial.
2. `/index` — página inicial.
3. `/ola` — saudação.
4. `/ola/Joao` — parâmetro de rota.
5. `/contato` — contato.
6. `/usuario` — perfil.
7. `/usuario/Joao/Estudante/Desenvolvimento%20Web%20III` — perfil com parâmetros.
8. `/login` — formulário de login.
9. Login válido: `joao` / `flask2026`.
10. Login inválido — redirecionamento para `/login` com mensagem flash.
11. `POST /novocadastro/` — tela de novo cadastro.

## Observação
O ambiente de execução desta preparação não possui Flask instalado e não tem acesso de rede para instalar pacotes. Por isso, o teste HTTP real precisa ser concluído no ambiente local após instalar `requirements.txt`; a validação de sintaxe e do histórico Git foi executada aqui.
