import inject


def inject_dependencies(config_modules):

    # https://github.com/ivankorobkov/python-inject#usage-with-django
    def configure(binder: inject.Binder):
        for services in config_modules:
            if hasattr(services, "inject_dependencies"):
                binder.install(services.inject_dependencies)

    inject.configure_once(configure)
