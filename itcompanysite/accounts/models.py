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
        },
    )
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
    )

    # Добавляем поле для роли пользователя
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('company', 'Company'),
        ('educational_institution', 'Educational_institution')
    )
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default='student')

    def is_student(self):
        return self.role == 'student'

    def is_admin(self):
        return self.role == 'admin'

    def is_company(self):
        return self.role == 'company'

    def is_educational_institution(self):
        return self.role == 'educational_institution'
