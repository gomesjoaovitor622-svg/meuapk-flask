"""Ponto de entrada WSGI para Gunicorn/uWSGI."""

from app import create_app

app = create_app()
