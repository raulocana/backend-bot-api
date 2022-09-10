import uuid

from django.contrib.auth import get_user_model
from django.db.models import (
    SET_NULL,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    TextChoices,
    TextField,
    UUIDField,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Ticket(Model):
    class Topics(TextChoices):
        SALES = "SALES", "Sales"
        PRICING = "PRICING", "Pricing"
        OTHER = "OTHER", "Other"

    uuid = UUIDField(
        _("UUID"),
        unique=True,
        null=False,
        default=uuid.uuid4,
        editable=False,
    )

    user = ForeignKey(
        to=User,
        to_field="uuid",
        on_delete=SET_NULL,
        verbose_name=_("user"),
        null=True,
    )

    topic = CharField(
        _("Topic"),
        max_length=32,
        null=False,
        choices=Topics.choices,
        default=Topics.OTHER,
    )

    question = TextField(
        _("Question"),
        max_length=1024,
        blank=True,
        null=False,
    )

    date_created = DateTimeField(_("Date created"), default=timezone.now)

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
