from django.db import models
from companies.models import Company, CompanyAddress


class Internship(models.Model):

    all_places = models.IntegerField('all_places')
    available_places = models.IntegerField('available_places')
    time_type_work = models.TextField('time_type_work')
    date_start = models.DateField('date_start')
    date_end = models.DateField('date_end')
    salary = models.IntegerField('salary')
    description = models.TextField('description', default="")
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,  default='')
    company_address = models.ForeignKey(CompanyAddress, on_delete=models.DO_NOTHING, default='')

