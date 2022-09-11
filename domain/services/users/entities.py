from domain.services.common.entities import Entity


class UserEntity(Entity):
    entity_name = "UserEntity"

    def __init__(
        self,
        uuid: str = None,
        name: str = None,
        email: str = None,
        phone: str = None,
        origin: str = None,
    ):
        self._uuid = uuid
        self._name = name
        self._email = email
        self._phone = phone
        self._origin = origin

    @property
    def uuid(self) -> str:
        return self._uuid

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def origin(self) -> str:
        return self._origin

    def update(
        self,
        name: str = None,
        phone: str = None,
        origin: str = None,
    ):
        if name is not None:
            self._name = name
        if phone is not None:
            self._phone = phone
        if origin is not None:
            self._origin = origin
