from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    email_verify = models.BooleanField(default=False)

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("Пользователь с такой почтой уже зарегистрирован."),
        },)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
    )
