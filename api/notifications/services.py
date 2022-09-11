from inject import Binder

from domain.services.notifications.interactors import (
    SendMailInterator,
    SendWelcomeMailInteractor,
)


def inject_dependencies(binder: Binder):

    # Interactors
    binder.bind(SendMailInterator, SendMailInterator())
    binder.bind(SendWelcomeMailInteractor, SendWelcomeMailInteractor())
