from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class University(models.Model):
    name = models.TextField('name')
    description = models.TextField('description')
    url = models.TextField('url')
    phone = models.TextField('phone')

class UniversityUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)