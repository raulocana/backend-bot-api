from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.users.serializers import CreateUserRequestSerializer


class UserViewSet(CreateModelMixin, GenericViewSet):
    def get_serializer_class(self):
        match self.action:
            case "create":
                return CreateUserRequestSerializer
            case _:
                return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        """Basic user creation or update, obfuscates if user already exists"""
        User = get_user_model()
        try:
            user = User.objects.get(email=serializer.validated_data.get("email"))
            user.name = serializer.validated_data.get("name")
            user.phone = serializer.validated_data.get("phone")
            user.save()
        except Exception:
            user = User.objects.create(**serializer.validated_data)
            # run async task for send welcome email.

        return Response({"uuid": user.uuid})
