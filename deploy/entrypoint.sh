#!/bin/sh
# Executa as migrações antes de subir o servidor.
set -eu

flask db upgrade

exec "$@"
