from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.tickets.serializers import CreateTicketRequestSerializer
from domain.services.tickets.interactors import CreateTicketInteractor


class TicketViewSet(CreateModelMixin, GenericViewSet):

    create_ticket_interactor = CreateTicketInteractor()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return CreateTicketRequestSerializer
            case _:
                return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ticket = self.create_ticket_interactor.execute(**serializer.validated_data)

        return Response({"uuid": ticket.uuid})
