import inject
from celery import Task

from domain.services.notifications.interactors import SendWelcomeMailInteractor


class SendWelcomeMailTask(Task):

    name = "send_welcome_mail_task"

    send_welcome_mail_interactor = inject.attr(SendWelcomeMailInteractor)

    def execute(self, email: str, user_name: str = None):
        self.apply_async(args=[email, user_name], countdown=60, retry=True)

    def run(self, email: str, user_name: str = None, *args, **kwargs):
        self.send_welcome_mail_interactor.execute(
            email=email, user_name=user_name, *args, **kwargs
        )
