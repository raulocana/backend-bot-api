import inject

from domain.services.common.exceptions import DoesNotExistException
from domain.services.users.datasources import UserDatasourceInterface
from domain.services.users.entities import UserEntity


class UserRepository:

    user_datasource = inject.attr(UserDatasourceInterface)

    def save(self, user: UserEntity) -> UserEntity:
        return self.user_datasource.save(user)

    def get_by_uuid(self, uuid: str) -> UserEntity | None:
        try:
            return self.user_datasource.get_by_uuid(uuid)
        except DoesNotExistException:
            return None

    def get_by_email(self, email: str) -> UserEntity | None:
        try:
            return self.user_datasource.get_by_email(email)
        except DoesNotExistException:
            return None
