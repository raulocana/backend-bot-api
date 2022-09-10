from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import Serializer


class CreateUserRequestSerializer(Serializer):
    name = CharField(min_length=2, max_length=128)
    email = EmailField()
    phone = CharField(min_length=4, max_length=32)
    origin = CharField(min_length=2, max_length=32, required=False)
