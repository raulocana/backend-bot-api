from enum import Enum

from domain.services.common.entities import Entity


class TicketEntity(Entity):
    entity_name = "Ticket"

    class Topics(Enum):
        SALES = "SALES"
        PRICING = "PRICING"
        OTHER = "OTHER"

        @classmethod
        def from_str(cls, value: str):
            for topic in list(cls):
                if topic.value == value.upper():
                    return topic
            return cls.OTHER

    def __init__(
        self,
        uuid: str = None,
        user_uuid: str = None,
        topic: str = None,
        question: str = None,
    ):
        self._uuid = uuid
        self._user_uuid = user_uuid
        self._topic = topic
        self._question = question

    @property
    def uuid(self) -> str:
        return self._uuid

    @property
    def user_uuid(self) -> str:
        return self._user_uuid

    @property
    def topic(self) -> str:
        return self._topic

    @property
    def question(self) -> str:
        return self._question
