from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import CharField
from django.forms import PasswordInput
from django import forms

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
