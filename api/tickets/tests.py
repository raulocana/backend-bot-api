from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from api.tickets.models import Ticket


class TicketTests(TestCase):
    User = get_user_model()

    def test_create_ticket_blank_question(self):
        user = self.User.objects.create_user(
            name="Test User",
            email="test@email.com",
            phone="+34 555 55 55 55",
            origin="Spain",
        )

        ticket = Ticket.objects.create(
            user=user,
            topic=Ticket.Topics.SALES,
            question="",
        )

        self.assertEqual(ticket.user.uuid, user.uuid)
        self.assertEqual(ticket.topic, Ticket.Topics.SALES)
        self.assertEqual(ticket.question, "")
        self.assertLess(ticket.date_created, timezone.now())

    def test_create_ticket_with_question(self):
        user = self.User.objects.create_user(
            name="Test User",
            email="test@email.com",
            phone="+34 555 55 55 55",
            origin="Spain",
        )

        ticket = Ticket.objects.create(
            user=user,
            topic=Ticket.Topics.PRICING,
            question="This is a test question\nwith more than one line\nof text.",
        )

        self.assertEqual(ticket.user.uuid, user.uuid)
        self.assertEqual(ticket.topic, Ticket.Topics.PRICING)
        self.assertEqual(
            ticket.question,
            "This is a test question\nwith more than one line\nof text.",
        )
        self.assertLess(ticket.date_created, timezone.now())

    def test_create_ticket_with_other_topic(self):
        user = self.User.objects.create_user(
            name="Test User",
            email="test@email.com",
            phone="+34 555 55 55 55",
            origin="Spain",
        )

        ticket = Ticket.objects.create(
            user=user,
            topic=Ticket.Topics.OTHER,
            question="test question",
        )

        self.assertEqual(ticket.user.uuid, user.uuid)
        self.assertEqual(ticket.topic, Ticket.Topics.OTHER)
        self.assertEqual(ticket.question, "test question")
        self.assertLess(ticket.date_created, timezone.now())
