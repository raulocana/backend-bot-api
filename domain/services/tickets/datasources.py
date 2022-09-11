from abc import ABC, abstractmethod

from domain.services.tickets.entities import TicketEntity


class TicketDatasourceInterface(ABC):
    @abstractmethod
    def save(self, ticket_entity: TicketEntity) -> TicketEntity:
        pass
