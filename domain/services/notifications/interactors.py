from django.core.mail import send_mail


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
