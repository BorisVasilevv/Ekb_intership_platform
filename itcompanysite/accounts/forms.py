from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .utils import send_email_for_verify
from companies.models import Company, City, Address, CompanyAddress, CompanyUser
from internships.models import StudentResponse
from .models import File
from companies.utils import geocoder

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
        required=False,
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
    phone = forms.CharField(
        label=_("Телефон"),
        max_length=20,
        widget=forms.TextInput(attrs={"autocomplete": "phone"}),
    )
    location = forms.CharField(
        label=_("Местоположение (город, улица, номер дома)"),
        max_length=255,
        widget=forms.TextInput(attrs={"autocomplete": "location"}),
        required=False,
    )
    company_name = forms.CharField(
        label=_("Название компании"),
        max_length=255,
        widget=forms.TextInput(attrs={"autocomplete": "company_name"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "phone", "location", "company_name", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            # Установите роль здесь
            user.role = self.cleaned_data.get('role')
            user.save()

            # Создаем компанию
            company = Company.objects.create(
                name=self.cleaned_data.get('company_name'),
                phone=self.cleaned_data.get('phone'),
                short_description="Описание компании",  # Или динамически
                url="https://example.com",  # Или получить из формы
            )

            # Создаем адрес на основе поля location
            location_data = self.cleaned_data.get('location').split(', ')
            city_name = location_data[0]
            street_name = location_data[1] if len(location_data) > 1 else ""
            house_number = location_data[2] if len(location_data) > 2 else ""

            coordinates = geocoder(city_name)
            coordinates2 = geocoder(location_data)
            city, _ = City.objects.get_or_create(name=city_name, coordinate_x=coordinates[0], coordinate_y=coordinates[1])
            address = Address.objects.create(
                city=city,
                street=street_name,
                home_number=house_number,
                coordinate_x=coordinates2[0],
                coordinate_y=coordinates2[1],
            )

            # Связываем компанию с адресом
            CompanyAddress.objects.create(company=company, address=address)

            # Опционально связываем компанию с пользователем
            CompanyUser.objects.create(user=user, company=company)
        return user
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


class StudentResponseForm(forms.ModelForm):
    files = forms.ModelMultipleChoiceField(
        queryset=File.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Выберите файлы"
    )
    response_text = forms.CharField(widget=forms.Textarea, label="Текст отклика", required=False)

    class Meta:
        model = StudentResponse
        fields = ['response_text', 'files']

