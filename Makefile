install:
	poetry install

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

lint:
	poetry run flake8 task_manager

upd_locale:
	poetry run django-admin makemessages --locale=ru

compile_locale:
	poetry run django-admin compilemessages

make_migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate