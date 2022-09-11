from inject import Binder

from api.tickets.data.datasource import TicketDatasource
from domain.services.tickets.datasources import TicketDatasourceInterface
from domain.services.tickets.interactors import CreateTicketInteractor
from domain.services.tickets.repositories import TicketRepository


def inject_dependencies(binder: Binder):

    # Datasources
    binder.bind(TicketDatasourceInterface, TicketDatasource())

    # Repositories
    binder.bind(TicketRepository, TicketRepository())

    # Interactors
    binder.bind(CreateTicketInteractor, CreateTicketInteractor())
