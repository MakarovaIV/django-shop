from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput, EmailInput

from grocery.models import Category, Product


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=PasswordInput)
    password2 = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    desc = forms.CharField(max_length=500)
    composition = forms.CharField(max_length=500)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    units = forms.CharField(max_length=10)
    picture = forms.ImageField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form_class'
    }))

    class Meta:
        model = Product
        fields = ['name', 'desc', 'composition', 'price', 'picture', 'category', 'units']


class Cart(forms.ModelForm):
    total_price = forms.FloatField(disabled=True)
    total_count = forms.IntegerField(disabled=True)
