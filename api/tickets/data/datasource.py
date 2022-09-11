from django.db import IntegrityError

from api.tickets.models import Ticket
from domain.services.common.exceptions import IntegrityErrorException
from domain.services.tickets.datasources import TicketDatasourceInterface
from domain.services.tickets.entities import TicketEntity


class TicketDatasource(TicketDatasourceInterface):
    @staticmethod
    def _map_orm_ticket_to_entity(orm_ticket: Ticket) -> TicketEntity:
        return TicketEntity(
            uuid=str(orm_ticket.uuid),
            user_uuid=str(orm_ticket.user.uuid),
            topic=orm_ticket.topic,
            question=orm_ticket.question,
        )

    @staticmethod
    def _update_orm_ticket_from_entity(orm_ticket: Ticket, ticket_entity: TicketEntity):
        orm_ticket.topic = ticket_entity.topic
        orm_ticket.question = ticket_entity.question

    def _create_orm_ticket(self, ticket_entity: TicketEntity) -> Ticket:
        try:
            orm_ticket = Ticket.objects.create(
                user_id=ticket_entity.user_uuid,
                topic=ticket_entity.topic,
                question=ticket_entity.question,
            )
            return orm_ticket
        except Exception as e:
            print(e)
            raise IntegrityErrorException(TicketEntity)

    def _update_orm_ticket(self, ticket_entity: TicketEntity) -> Ticket:
        try:
            orm_ticket = Ticket.objects.get(uuid=ticket_entity.uuid)
            self._update_orm_ticket_from_entity(orm_ticket, ticket_entity)
            orm_ticket.save()
            return orm_ticket
        except IntegrityError:
            raise IntegrityErrorException(TicketEntity)

    def save(self, ticket_entity: TicketEntity) -> TicketEntity:
        if ticket_entity.uuid is not None:
            orm_user = self._update_orm_ticket(ticket_entity)
        else:
            orm_user = self._create_orm_ticket(ticket_entity)
        return self._map_orm_ticket_to_entity(orm_user)
