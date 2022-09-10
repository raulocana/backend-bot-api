from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.tickets.models import Ticket
from api.tickets.serializers import CreateTicketRequestSerializer


class TicketViewSet(CreateModelMixin, GenericViewSet):
    def get_serializer_class(self):
        match self.action:
            case "create":
                return CreateTicketRequestSerializer
            case _:
                return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        """Basic user creation or update, obfuscates if user already exists"""
        User = get_user_model()
        try:
            user = User.objects.get(uuid=serializer.validated_data.get("user_uuid"))
        except Exception:
            return Response({"error": "User does not exist"}, status=400)
        else:
            ticket = Ticket.objects.create(
                user=user,
                topic=serializer.validated_data.get("topic"),
                question=serializer.validated_data.get("question"),
            )
            # Send event to propagate notifications

        return Response({"uuid": ticket.uuid})
