from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .utils import send_email_for_verify

User = get_user_model()
class StudentCreationForm(UserCreationForm):

    """Method which let username be not unique"""
    def clean_username(self):
        return self.cleaned_data.get("username")

    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "role")

        # if only email
        # fields = ("email",)

class EducationCreationForm(UserCreationForm):

    """Method which let username be not unique"""
    def clean_username(self):
        return self.cleaned_data.get("username")

    phone = forms.CharField(
        label=_("Телефон"),
        max_length=20,
        widget=forms.TextInput(attrs={"autocomplete": "phone"}),
    )
    location = forms.CharField(
        label=_("Местоположение"),
        max_length=255,
        widget=forms.TextInput(attrs={"autocomplete": "location"}),
    )
    company_name = forms.CharField(
        label=_("Название образовательного учреждения"),
        max_length=255,
        widget=forms.TextInput(attrs={"autocomplete": "company_name"}),
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "phone", "location", "company_name", "role")

class CompanyCreationForm(UserCreationForm):
    def clean_username(self):
        return self.cleaned_data.get("username")

    phone = forms.CharField(
        label=_("Телефон"),
        max_length=20,
        widget=forms.TextInput(attrs={"autocomplete": "phone"}),
    )
    location = forms.CharField(
        label=_("Местоположение"),
        max_length=255,
        widget=forms.TextInput(attrs={"autocomplete": "location"}),
    )
    company_name = forms.CharField(
        label=_("Название компании"),
        max_length=255,
        widget=forms.TextInput(attrs={"autocomplete": "company_name"}),
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "phone", "location", "company_name", "role")

class MyAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            elif not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Email не подтверждён! Письмо выслано ещё раз. Проверьте Ваш email, возможно письмо попало в папку спам!',
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
