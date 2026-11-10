# Política de segurança

## Versões suportadas

Apenas a branch `main` recebe correções de segurança.

## Como reportar uma vulnerabilidade

Não abra uma issue pública. Envie um e-mail para o mantenedor do repositório
com:

- descrição da falha e impacto;
- passos para reproduzir;
- versão/commit afetado;
- sugestão de correção, se houver.

Você receberá uma resposta em até 7 dias. Após a correção, o crédito será
dado no changelog, se desejado.

## Práticas adotadas

- Senhas armazenadas com `scrypt` (Werkzeug), nunca em texto puro.
- Login apenas por `POST`, com proteção CSRF.
- Sessão em cookie `HttpOnly` + `SameSite=Lax` (`Secure` em produção).
- Rate limit de 5 tentativas por minuto no login.
- `SECRET_KEY` obrigatória e vinda do ambiente.
- Dependências fixadas com hash (`pip install --require-hashes`).
- `pip-audit`, `detect-secrets` e CodeQL no CI.
- Container roda como usuário não-root, com `cap_drop: ALL` e filesystem read-only.
