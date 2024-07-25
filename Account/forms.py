from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput
from .models import User
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'phone_number', 'address', 'city', 'subcity', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username', 'autofocus': True}),
            'firstname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'lastname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'subcity': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your subcity'}),
            'password1': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'password2': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email
    # def clean(self):
    #     cleaned_data = super().clean()
    #     if not cleaned_data.get('terms'):
    #         raise ValidationError('You must agree to the terms and conditions.')
    #     return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'name': 'email-username',
            'placeholder': 'Enter your username',
            'autofocus': True
        })
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password',
            'name': 'password',
            'placeholder': '&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;'
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'remember-me'
        })
    )