from django.views.generic import TemplateView
from . import views
from django.urls import path, include
from .views import EmailView, MyLoginView, upload_document

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),

    path('', include('django.contrib.auth.urls')),
    path('registration/', views.registration, name='registration'),
    path('registration/student', views.registration, name='student_reg'),
    path('registration/company', views.registration, name='company_reg'),
    path('registration/ed_institution', views.registration, name='ed_institution'),
    path('profile/', views.profile, name='profile'),
    path('profile/upload/', upload_document, name='upload_document'),

    path(
        'invalid_verify/',
        TemplateView.as_view(template_name='accounts/invalid_verify.html'),
        name='invalid_verify'
    ),
    path(
        'confirm_email/',
        TemplateView.as_view(template_name='accounts/confirm_email.html'),
        name='confirm_email'
    ),
    path(
        'verify_email/<uidb64>/<token>/',
        EmailView.as_view(),
        name="verify_email",
    ),
    path('remove_from_favorites/<int:company_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]
