import inject

from api.tickets.data.datasource import TicketDatasource
from domain.services.common.exceptions import DoesNotExistException
from domain.services.tickets.entities import TicketEntity


class TicketRepository:

    ticket_datasource = inject.attr(TicketDatasource)

    def save(self, ticket: TicketEntity) -> TicketEntity:
        return self.ticket_datasource.save(ticket)

    def get_by_uuid(self, uuid: str) -> TicketEntity | None:
        try:
            return self.ticket_datasource.get_by_uuid(uuid)
        except DoesNotExistException:
            return None
