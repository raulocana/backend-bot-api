import inject
from celery import Celery
from inject import Binder

from api.notifications.tasks import SendWelcomeMailTask
from domain.services.notifications.interactors import (
    SendMailInterator,
    SendWelcomeMailInteractor,
)


def inject_dependencies(binder: Binder):

    # Interactors
    binder.bind(SendMailInterator, SendMailInterator())
    binder.bind(SendWelcomeMailInteractor, SendWelcomeMailInteractor())

    # Tasks
    binder.bind(SendWelcomeMailTask, SendWelcomeMailTask())


def export_tasks(celery: Celery):
    celery.register_task(inject.instance(SendWelcomeMailTask))
