from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput, EmailInput

from grocery.models import Category, Product, Cart, Order


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
    picture = forms.CharField(required=False)

    class Meta:
        model = Category
        fields = ['name', 'picture']


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    desc = forms.CharField(max_length=500, required=False)
    composition = forms.CharField(max_length=500, required=False)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    units = forms.CharField(max_length=10)
    picture = forms.CharField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form_class'
    }))

    class Meta:
        model = Product
        fields = ['name', 'desc', 'composition', 'price', 'picture', 'category', 'units']


class CartForm(forms.ModelForm):
    total_price = forms.FloatField(disabled=True)
    total_count = forms.IntegerField(disabled=True)

    class Meta:
        model = Cart
        fields = ['total_price', 'total_count']


class MakeOrderForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    address = forms.CharField(label='Delivery address (City, Street, House, Flat)', max_length=500)
    payment_type = forms.ChoiceField(label='Choose payment type', choices=(("1", "Cash"), ("2", "Credit Card")))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'payment_type']


class OrderForm(forms.ModelForm):
    address = forms.CharField(label='Delivery address (City, Street, House, Flat)', max_length=500, disabled=True)
    payment_type = forms.ChoiceField(label='Choose payment type', choices=(("1", "Cash"), ("2", "Credit Card")),
                                     disabled=True)
    product_name = forms.CharField(label='Product name', max_length=500, disabled=True)

    class Meta:
        model = Order
        fields = ['address', 'payment_type', 'product_name']
