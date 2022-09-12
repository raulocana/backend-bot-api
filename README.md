# Landbot Backend Challenge

Landbot Backend Challenge API!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Context

This is a repository that aims to provide a Django Rest API for handling external requests from a Landbot bot, as an integration peer in the lead management process.

The project bootstraps from a Django Cookiecutter template, as this is the quickest and safest way to create a Django Rest API with production-ready features. From that template, all unrequired dependencies and modules have been removed, providing a final project both easy to maintain and lightweight.

All the contained features have been developed from a requirement standpoint. Thus, the project delivers the requested attributes with the best architecture and code scalability while maintaining the code base as shorter and maintainable as possible.

Mainly, you will find a Django + DRF API with four apps: the first two of them are in charge of managing the users and the tickets (for customer support, or another department); the third one handles notifications (email service or extra integrations); the last one focuses on dependency injection (taking advantage of the Django apps module loading process).

Both, the users and tickets apps, have basic tests to ensure all the DB operations can be safely performed within the requested features for the API.

In the background, there are other services also supporting the main one, such as a PostgreSQL DB, a Redis Queue (only for brokering asynchronous tasks, but potentially useful for the caching of domain entities), a Celery Worker plus a Celery Beat, and a MailHog service for local email management.

Thanks to the combination of Redis and Celery it is possible to handle asynchronous operations such as sending the welcome email (in this case with a 60-second delay, but without blocking the request thread), or sending various internal notifications using an asynchronous broker.

The broker, in this case, handles the topic within the expected scopes and creates an asynchronous task for each notification that shall be sent. These notifications are mimicked as emails because the span of the project does not provide external apps to connect with, but this approach makes different integrations decoupled from each other, so they are very easy to extend, as every external service may have its particular domain interactor and communication repository.

Every service is containerized, so horizontal scalability is directly obtainable through container replication. Also, this allows potential deployment on Kubernetes clusters where with just some deployment files it is possible to expose the complete service in production, having autoscaling capabilities and without compromising security (all the important secrets are intake as environment variables already).

Finally, an important disclaimer is that the project is not ready to be run in production mode, as it does not have TLS certificates (handled by Traefik and Let's Encrypt), or a production SMTP Server or External Service declared.

## Settings

It is essential that the environment variable `NGROK_EXTERNAL_URL` is set to the Ngrok URL that tunnels to your local service, this could be done using the `.django` env file at `.envs/.local` on the root project. If the service is running through a debugger, use the debugger running configuration to set it.

Also, the required Landbot bot builder used could be found [here](https://app.landbot.io/gui/bot/1552525/builder).

There is a Makefile file in the project root, where a commonly needed command could be found.

The project could be initialized with the command:

    $ make init

This command builds the containers, collects static files as for the admin panel, generate the necessary migrations and applies them, and finnaly start all the services in detached-mode.

Other useful commands are:

    $ make restart

    $ make showmigrations

    $ make createsuperuser


For the different favours of run-modes: `run-debug` starts all the services but Django, in order to running it from the IDE debugger; `run-verbose` starts all the services but in attached-mode.

    $ make run-debug

    $ make run-verbose

### Running tests

For tests running there is also a make command, which runs a separate container with the local configuration:

    $ make tests
