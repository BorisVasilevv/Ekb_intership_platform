from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_internship, name='create_internship'),
    path('', views.internships_list, name='internships_list'),  # Список стажировок

    # Маршрут для детального отображения стажировки
    path('internships/<int:internship_id>/', views.internship_detail, name='internship_detail'),
    ]
