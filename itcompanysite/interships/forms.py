from django import forms
from .models import Internship


class InternshipCreationForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = [
            'specialty', 'description', 'location', 'salary',
            'work_mode', 'start_date', 'end_date', 'number_of_positions'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
