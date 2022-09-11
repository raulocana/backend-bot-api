from enum import Enum

import inject
from celery import Task

from domain.services.common.exceptions import (
    UncontrolledIntegrationServiceException,
    UncontrolledTopicException,
)
from domain.services.notifications.interactors import SendInternalTicketMailInteractor
from domain.services.tickets.entities import TicketEntity
from domain.services.tickets.repositories import TicketRepository
from domain.services.users.repositories import UserRepository


class IntegrationServices(Enum):
    EMAIL = "EMAIL"
    SLACK = "SLACK"
    ASANA = "ASANA"
    HUBSPOT = "HUBSPOT"

    @classmethod
    def from_str(cls, value: str):
        for topic in list(cls):
            if topic.value == value.upper():
                return topic
        return None


class InternalMessagingBroker(Task):

    name = "internal_messaging_broker_task"

    user_repository = inject.attr(UserRepository)
    ticket_repository = inject.attr(TicketRepository)

    send_internal_ticket_mail_interactor = inject.attr(SendInternalTicketMailInteractor)

    topic_integration_map = {
        TicketEntity.Topics.SALES: [
            IntegrationServices.EMAIL,
            IntegrationServices.HUBSPOT,
        ],
        TicketEntity.Topics.PRICING: [
            IntegrationServices.EMAIL,
            IntegrationServices.SLACK,
        ],
        TicketEntity.Topics.OTHER: [
            IntegrationServices.EMAIL,
            IntegrationServices.SLACK,
            IntegrationServices.HUBSPOT,
            IntegrationServices.ASANA,
        ],
    }

    def execute(self, topic_list: list[str], ticket_uuid: str):
        if not any(
            [
                TicketEntity.Topics.from_str(topic) in self.topic_integration_map
                for topic in topic_list
            ]
        ):
            raise UncontrolledTopicException

        integration_services = list(
            {
                it_serv
                for topic in topic_list
                for it_serv in self.topic_integration_map.get(
                    TicketEntity.Topics.from_str(topic), []
                )
            }
        )

        for it_serv in integration_services:
            self.apply_async(args=[it_serv.value, ticket_uuid], retry=True)

    def run(self, it_serv: str, ticket_uuid: str, *args, **kwargs):

        integration_interactor_map = {
            IntegrationServices.EMAIL: self.send_internal_ticket_mail_interactor,
            IntegrationServices.SLACK: self.send_internal_ticket_mail_interactor,
            IntegrationServices.ASANA: self.send_internal_ticket_mail_interactor,
            IntegrationServices.HUBSPOT: self.send_internal_ticket_mail_interactor,
        }

        integration_service = IntegrationServices.from_str(it_serv)
        if not integration_service:
            raise UncontrolledIntegrationServiceException

        ticket = self.ticket_repository.get_by_uuid(ticket_uuid)
        user = self.user_repository.get_by_uuid(ticket.user_uuid)

        interactor = integration_interactor_map.get(integration_service)
        interactor.execute(integration_service.value, user, ticket)
