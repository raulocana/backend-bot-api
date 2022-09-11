from inject import Binder

from api.users.data.datasource import UserDatasource
from domain.services.users.datasources import UserDatasourceInterface
from domain.services.users.interactors import CreateOrUpdateUserInteractor
from domain.services.users.repositories import UserRepository


def inject_dependencies(binder: Binder):

    # Datasources
    binder.bind(UserDatasourceInterface, UserDatasource())

    # Repositories
    binder.bind(UserRepository, UserRepository())

    # Interactors
    binder.bind(CreateOrUpdateUserInteractor, CreateOrUpdateUserInteractor())
