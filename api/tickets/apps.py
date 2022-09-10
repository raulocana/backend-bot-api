from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TicketsConfig(AppConfig):
    name = "api.tickets"
    verbose_name = _("Tickets")

    def ready(self):
        try:
            import api.tickets.signals  # noqa F401
        except ImportError:
            pass
