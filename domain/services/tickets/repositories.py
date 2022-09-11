import inject

from api.tickets.data.datasource import TicketDatasource
from domain.services.tickets.entities import TicketEntity


class TicketRepository:

    ticket_datasource = inject.attr(TicketDatasource)

    def save(self, ticket: TicketEntity) -> TicketEntity:
        return self.ticket_datasource.save(ticket)
