from account.models import Users
from django.forms import ModelForm, PasswordInput, EmailInput



class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']

        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email',
                'name': 'email',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'name': 'password',
            })
        }