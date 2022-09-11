from api.users.data.datasource import UserDatasource
from domain.services.common.exceptions import DoesNotExistException
from domain.services.users.entities import UserEntity


class UserRepository:

    user_datasource = (
        UserDatasource()
    )  # TODO: inject as dependency, invoking the interface

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
