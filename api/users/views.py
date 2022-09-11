import inject
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.users.serializers import CreateUserRequestSerializer
from domain.services.users.interactors import CreateOrUpdateUserInteractor


class UserViewSet(CreateModelMixin, GenericViewSet):

    create_or_update_user_interactor = inject.instance(CreateOrUpdateUserInteractor)

    def get_serializer_class(self):
        match self.action:
            case "create":
                return CreateUserRequestSerializer
            case _:
                return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.create_or_update_user_interactor.execute(
            **serializer.validated_data
        )

        return Response({"uuid": user.uuid})
