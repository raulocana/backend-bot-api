import inject

from config import celery_app


def inject_dependencies(config_modules):

    # https://github.com/ivankorobkov/python-inject#usage-with-django
    def configure(binder: inject.Binder):
        for services in config_modules:
            if hasattr(services, "inject_dependencies"):
                binder.install(services.inject_dependencies)

    inject.configure_once(configure)


def export_tasks(config_modules):
    for services in config_modules:
        if hasattr(services, "export_tasks"):
            services.export_tasks(celery_app)
