from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Internship)
admin.site.register(Specialization)
admin.site.register(InternshipSpecialization)
admin.site.register(StudentResponse)
admin.site.register(StudentResponseFile)
admin.site.register(FavoriteInternship)
