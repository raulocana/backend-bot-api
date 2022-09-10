import uuid as uuid

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import CharField, EmailField, UUIDField
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None  # type: ignore
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    uuid = UUIDField(
        _("UUID"), unique=True, null=False, default=uuid.uuid4, editable=False
    )

    name = CharField(_("Name"), blank=False, max_length=128)

    email = EmailField(_("Email address"), unique=True, blank=False)

    phone = CharField(_("Phone number"), blank=False, max_length=32)

    USERNAME_FIELD = "email"

    # Email field is imposed as required, as it is being used as the username field.
    REQUIRED_FIELDS = ["name", "phone"]

    objects = CustomUserManager()
