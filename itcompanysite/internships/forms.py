from django import forms
from .models import Internship


class InternshipCreationForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = [
            'all_places', 'available_places', 'time_type_work',
            'date_start', 'date_end', 'salary', 'description',
            'company', 'company_address'
        ]
        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date'}),
            'date_end': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
