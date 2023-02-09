from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput, EmailInput


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=PasswordInput)
    password2 = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
