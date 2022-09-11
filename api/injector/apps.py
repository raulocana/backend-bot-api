from importlib import import_module

from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from api.injector.services import inject_dependencies


class InjectorConfig(AppConfig):
    name = "api.injector"
    verbose_name = _("Injector")

    def ready(self) -> None:
        config_modules = self._get_app_config_modules()
        inject_dependencies(config_modules)

    @staticmethod
    def _get_app_config_modules():
        app_config_modules = []
        for app in settings.LOCAL_APPS:
            try:
                services = import_module(f"{app}.services")
                app_config_modules.append(services)
            except ImportError:
                raise ImportError(
                    f"Service module does not exist on {app} app. Execution aborted."
                )
        return app_config_modules
