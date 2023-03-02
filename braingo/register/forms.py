from .models import Users
from django.forms import ModelForm, PasswordInput, EmailInput


class RegistrationForm(ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']

        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту',
                'name': 'email',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
                'name': 'password'
            }),
        }