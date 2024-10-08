from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import CharField
from django.forms import PasswordInput
from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'url', 'image']  # Поля, которые будут в форме
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка на новость'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class UserRegistrationForm(ModelForm):
    username = CharField(label='Имя пользователя',  widget=forms.TextInput)
    password1 = CharField(label='Пароль',  widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password1')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-input'}),
            'password1': forms.PasswordInput(attrs={'class':'form-input'})
        }

        def __init__(self, *args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].widgets.attrs.update({'class':'registration-help-info'})
