.PHONY: install run test lint fmt seed migrate docker docker-down

install:
	pip install -r requirements-dev.txt

run:
	python run.py

test:
	pytest

lint:
	ruff check .
	ruff format --check .

fmt:
	ruff format .
	ruff check --fix .

seed:
	python -m scripts.seed

migrate:
	FLASK_APP=wsgi.py flask db upgrade

docker:
	docker compose -f deploy/docker-compose.yml up --build

docker-down:
	docker compose -f deploy/docker-compose.yml down
