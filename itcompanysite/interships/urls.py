from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_internship, name='create_internship'),
    path('', views.internship_list, name='internships'),  # например, список стажировок
]
