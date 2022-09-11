import inject
from celery import Celery
from inject import Binder

from api.notifications.tasks import SendWelcomeMailTask
from domain.services.notifications.broker import InternalMessagingBroker
from domain.services.notifications.interactors import (
    SendInternalTicketMailInteractor,
    SendMailInterator,
    SendWelcomeMailInteractor,
)


def inject_dependencies(binder: Binder):

    # Interactors
    binder.bind(SendMailInterator, SendMailInterator())
    binder.bind(SendWelcomeMailInteractor, SendWelcomeMailInteractor())
    binder.bind(SendInternalTicketMailInteractor, SendInternalTicketMailInteractor())

    # Tasks
    binder.bind(InternalMessagingBroker, InternalMessagingBroker())
    binder.bind(SendWelcomeMailTask, SendWelcomeMailTask())


def export_tasks(celery: Celery):
    celery.register_task(inject.instance(InternalMessagingBroker))
    celery.register_task(inject.instance(SendWelcomeMailTask))
