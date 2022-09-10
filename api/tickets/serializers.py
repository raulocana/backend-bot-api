from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, UUIDField
from rest_framework.serializers import Serializer

from api.tickets.models import Ticket


class CreateTicketRequestSerializer(Serializer):
    user_uuid = UUIDField()
    topic = CharField(max_length=32)
    question = CharField(max_length=1024, allow_blank=True)

    def validate_topic(self, topic: str):
        topic_upper = topic.upper()

        if topic_upper not in [choice for choice, label in Ticket.Topics.choices]:
            raise ValidationError(
                detail=_(f"'{topic}' is not a valid topic"),
            )
        return topic_upper
