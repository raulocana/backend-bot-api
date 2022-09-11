import inject

from domain.services.common.exceptions import DoesNotExistException
from domain.services.tickets.entities import TicketEntity
from domain.services.tickets.repositories import TicketRepository
from domain.services.users.entities import UserEntity
from domain.services.users.repositories import UserRepository


class CreateTicketInteractor:

    user_repository = inject.attr(UserRepository)
    ticket_repository = inject.attr(TicketRepository)

    def execute(self, user_uuid: str, topic: str, question: str) -> TicketEntity:
        user = self.user_repository.get_by_uuid(user_uuid)
        if user is None:
            raise DoesNotExistException(UserEntity)
        ticket = TicketEntity(
            user_uuid=user.uuid,
            topic=topic,
            question=question,
        )
        ticket = self.ticket_repository.save(ticket)
        self._send_ticket_notifications(ticket)
        return ticket

    def _send_ticket_notifications(self, ticket: TicketEntity):
        # TODO: Complete the internal notification logic
        pass
