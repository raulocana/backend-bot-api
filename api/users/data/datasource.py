from django.contrib.auth import get_user_model
from django.db import IntegrityError

from domain.services.common.exceptions import (
    DoesNotExistException,
    IntegrityErrorException,
)
from domain.services.users.datasources import UserDatasourceInterface
from domain.services.users.entities import UserEntity

User = get_user_model()


class UserDatasource(UserDatasourceInterface):
    @staticmethod
    def _map_orm_user_to_entity(orm_user: User) -> UserEntity:
        return UserEntity(
            uuid=str(orm_user.uuid),
            name=orm_user.name,
            email=orm_user.email,
            phone=orm_user.phone,
            origin=orm_user.origin,
        )

    @staticmethod
    def _update_orm_user_from_entity(orm_user: User, user_entity: UserEntity):
        orm_user.name = user_entity.name
        orm_user.phone = user_entity.phone
        orm_user.origin = user_entity.origin

    def _create_orm_user(self, user_entity: UserEntity) -> User:
        try:
            orm_user = User.objects.create(
                name=user_entity.name,
                email=user_entity.email,
                phone=user_entity.phone,
                origin=user_entity.origin,
            )
            return orm_user
        except IntegrityError:
            raise IntegrityErrorException(UserEntity)

    def _update_orm_user(self, user_entity: UserEntity) -> User:
        try:
            orm_user = User.objects.get(uuid=user_entity.uuid)
            self._update_orm_user_from_entity(orm_user, user_entity)
            orm_user.save()
            return orm_user
        except IntegrityError:
            raise IntegrityErrorException(UserEntity)

    def save(self, user_entity: UserEntity) -> UserEntity:
        if user_entity.uuid is not None:
            orm_user = self._update_orm_user(user_entity)
        else:
            orm_user = self._create_orm_user(user_entity)
        return self._map_orm_user_to_entity(orm_user)

    def get_by_uuid(self, uuid: str) -> UserEntity:
        try:
            orm_user = User.objects.get(uuid=uuid)
            return self._map_orm_user_to_entity(orm_user)
        except User.DoesNotExist:
            raise DoesNotExistException(UserEntity)

    def get_by_email(self, email: str) -> UserEntity:
        try:
            orm_user = User.objects.get(email=email)
            return self._map_orm_user_to_entity(orm_user)
        except User.DoesNotExist:
            raise DoesNotExistException(UserEntity)
