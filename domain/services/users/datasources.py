from abc import ABC, abstractmethod

from domain.services.users.entities import UserEntity


class UserDatasourceInterface(ABC):
    @abstractmethod
    def save(self, user_entity: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_uuid(self, uuid: str) -> UserEntity:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity:
        pass
