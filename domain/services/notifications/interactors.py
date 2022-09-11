from django.core.mail import send_mail

from config.settings.base import INTERNAL_DISTRIBUTION_EMAIL
from domain.services.tickets.entities import TicketEntity
from domain.services.users.entities import UserEntity


class SendMailInterator:

    default_subject = "[UmiShop] You have a notification!"
    default_from_email = "no-reply@umishop.com"

    def execute(
        self,
        email_recipients: list[str],
        body: str,
        html_message: str = None,
        subject: str = None,
        from_email: str = None,
        fail_silently: bool = False,
    ):
        send_mail(
            subject or self.default_subject,
            body,
            from_email or self.default_from_email,
            email_recipients,
            html_message=html_message,
            fail_silently=fail_silently,
        )


class SendWelcomeMailInteractor(SendMailInterator):

    default_subject = "[UmiShop] Welcome to UmiShop!"

    body_message = "Hi{user_name},\n\nWe are very happy to welcome you to UmiShop :)\n\nThe UmiShop team!"

    def execute(self, email: str, user_name: str = None, *args, **kwargs):
        name = " " + user_name if user_name else ""

        body = self.body_message.format(user_name=name)
        super().execute(email_recipients=[email], body=body, *args, **kwargs)


class SendInternalTicketMailInteractor(SendMailInterator):

    default_from_email = "no-reply@internal.umishop.com"
    internal_to_email = INTERNAL_DISTRIBUTION_EMAIL

    subject_message = (
        "[New Ticket on {integration_name}] {topic} - {user_email} - {ticket_uuid}"
    )

    body_message = """

    A new ticket has been assigned for the {ticket_topic} topic. Details below:

    - User name: {user_name}
    - User mail: {user_email}
    - User phone: {user_phone}
    - User origin: {user_origin}

    - Ticket ID: {ticket_uuid}
    - Ticket topic: {ticket_topic}
    - Ticket question:

    \"{ticket_question}\"



    NOTE: This is an automatic notification, please do not reply to this sender.

    """

    def execute(
        self,
        integration_name: str,
        user: UserEntity,
        ticket: TicketEntity,
        *args,
        **kwargs
    ):
        subject = self.subject_message.format(
            integration_name=integration_name,
            topic=ticket.topic,
            user_email=user.email,
            ticket_uuid=ticket.uuid,
        )

        body = self.body_message.format(
            user_name=user.name,
            user_email=user.email,
            user_phone=user.phone,
            user_origin=user.origin,
            ticket_uuid=ticket.uuid,
            ticket_topic=ticket.topic,
            ticket_question=ticket.question,
        )
        super().execute(
            email_recipients=[self.internal_to_email],
            body=body,
            subject=subject,
            *args,
            **kwargs
        )
