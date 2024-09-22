from django.db import models
from companies.models import Company, CompanyAddress
from django.contrib.auth import get_user_model

User = get_user_model()
class Internship(models.Model):

    all_places = models.IntegerField('Всего мест')
    available_places = models.IntegerField('Доступных мест')
    time_type_work = models.TextField('Тип рабочего времени')
    date_start = models.DateField('Дата начала')
    date_end = models.DateField('Дата окончания')
    salary = models.IntegerField('Зарплата')
    description = models.TextField('Описание', default="")
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, default='', verbose_name='Компания')
    company_address = models.ForeignKey(CompanyAddress, on_delete=models.DO_NOTHING, default='', verbose_name='Адрес компании')


class Specialization(models.Model):
    specialization_name = models.TextField('specialization_name')

class InternshipSpecialization(models.Model):
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_DEFAULT, default='')
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, default='')

class StudentResponse(models.Model):
    studentResponseFiles = models.ForeignKey(User, on_delete=models.CASCADE,  default='')
    internship = models.ForeignKey(Internship, on_delete=models.DO_NOTHING,  default='')
    response_text = models.TextField('response_text')
    data_response = models.DateTimeField('data_response')


class FavoriteInternship(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.DO_NOTHING, default='')
    models.ForeignKey(User, on_delete=models.CASCADE, default='')