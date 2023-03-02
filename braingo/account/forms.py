from .models import Users
from django.forms import ModelForm, TextInput, EmailInput, FileInput, DateInput


class AccountForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'birthdate', 'profile_picture']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'name': 'name',
            }),
            'email': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту',
                'name': 'email',
            }),
            'birthdate': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год рождения',
                'name': 'birthdate',
            }),
            'profile_picture': FileInput(attrs={
                'class': 'form-control',
            })
        }