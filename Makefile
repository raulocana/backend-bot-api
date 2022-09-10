build:
	docker-compose -f local.yml build

run: build
	docker-compose -f local.yml up -d

run-verbose: build
	docker-compose -f local.yml up

down:
	docker-compose -f local.yml down

collectstatic: build
	docker-compose -f local.yml run --rm django python manage.py collectstatic

migrations: build
	docker-compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate

showmigrations:
	docker-compose -f local.yml run --rm django python manage.py showmigrations

createsuperuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

restart: down run

# This sequence assures that the project is ready to use from the first run
init: build collectstatic migrations migrate run
