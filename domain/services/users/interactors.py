import inject

from domain.services.users.entities import UserEntity
from domain.services.users.repositories import UserRepository


class CreateOrUpdateUserInteractor:

    user_repository = inject.attr(UserRepository)

    def execute(
        self, name: str, email: str, phone: str, origin: str = None
    ) -> UserEntity:
        user = self.user_repository.get_by_email(email)
        if not user:
            user = self._create_user(name, email, phone, origin)
            self._send_welcome_mail(user)
        else:
            self._update_user(user, name, phone, origin)
        return user

    def _create_user(
        self, name: str, email: str, phone: str, origin: str = None
    ) -> UserEntity:
        user = UserEntity(
            name=name,
            email=email,
            phone=phone,
            origin=origin,
        )
        user = self.user_repository.save(user)
        return user

    def _update_user(self, user: UserEntity, name: str, phone: str, origin: str = None):
        user.update(
            name=name,
            phone=phone,
            origin=origin,
        )
        self.user_repository.save(user)

    def _send_welcome_mail(self, user: UserEntity):
        # TODO: Complete the mail logic
        pass
