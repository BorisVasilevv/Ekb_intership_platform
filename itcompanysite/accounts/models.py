import uuid as uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import django.utils.timezone
from internships.models import Internship

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

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  default='')
    document_text = models.FileField('document_text', upload_to='files/' + str(uuid.uuid4()))
    created_at = models.DateTimeField('created_at', default=django.utils.timezone.now)
    document_name = models.TextField('document_name', default='file' + str(uuid.uuid4()))

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

class UserFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    file = models.ForeignKey(File, on_delete=models.CASCADE, default='')

class StudentResponse(models.Model):
    studentResponseFiles = models.ForeignKey(User, on_delete=models.CASCADE,  default='')
    internship = models.ForeignKey(Internship, on_delete=models.DO_NOTHING,  default='')
    response_text = models.TextField('response_text')
    data_response = models.DateTimeField('data_response')


class FavoriteInternship(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.DO_NOTHING, default='')
    models.ForeignKey(User, on_delete=models.CASCADE, default='')






