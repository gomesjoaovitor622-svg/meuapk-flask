# Atividade GitHub + Flask — Desenvolvimento Web III

Projeto construído a partir do código-base fornecido na aula, consolidando as versões `appFlask\\\_v1.py` até `appFlask\\\_v8.py` em **um único `app.py`**, conforme a atividade de controle de versões.

## Estrutura

* `app.py` — único arquivo Python da aplicação.
* `t\\\_templates/` — templates Flask com herança Jinja2.
* `templates/` — templates usados nas versões iniciais.
* `static/` — CSS e JavaScript da base da aula.
* `requirements.txt` — dependência Flask.
* `PESQUISA.md` — respostas da pesquisa solicitada no AVA.
* `EVIDENCIAS.md` — checklist de testes e prints.

## Como executar

```bash
python -m venv venv
venv\\\\\\\\Scripts\\\\\\\\activate
pip install -r requirements.txt
python app.py
```

Abra `http://127.0.0.1:7000`.

### Login de teste

* usuário: `joao`
* senha: `flask2026`

Também existem `alunoIFRO` e `visitante`, ambos com a senha `flask2026`.

## Histórico

O histórico Git registra a evolução baseada nas oito versões fornecidas na aula. A branch `aula6-heranca` contém a implementação de `base.html`, `{% extends %}`, `{% block %}` e `{% endblock %}`.

O ambiente virtual não deve ser versionado; `venv/` está no `.gitignore`.
Versão da branch aula6-heranca: templates com herança do template base.

