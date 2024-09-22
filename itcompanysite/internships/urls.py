from django.urls import path
from . import views
from .views import create_student_response

urlpatterns = [
    path('create/', views.create_internship, name='create_internship'),
    path('', views.internships_list, name='internships_list'),  # Список стажировок

    # Маршрут для детального отображения стажировки
    path('<int:internship_id>/', views.internship_detail, name='internship_detail'),
    path('<int:internship_id>/response/', create_student_response, name='create_student_response'),
    ]
