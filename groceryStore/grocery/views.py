import json
from datetime import datetime

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from grocery.forms import RegisterForm, CategoryForm, ProductForm, OrderForm
import django_filters
from .models import Category, Product, Cart, CartItem, Order


# def main_page(request):
#     categories = Category.objects.all()
#     context = {
#         'categories': categories
#     }
#     return render(request, 'grocery/category_list.html',  context=context)


class CategoryListView(ListView):
    model = Category
    template_name = 'grocery/category_list.html'
    context_object_name = 'categories'


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request=request, template_name="grocery/register_form.html", context={"register_form": form})


def login_handler(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("category")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="grocery/login.html", context={"login_form": form})


def logout_handler(request):
    if request.session:
        logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request=request, template_name="grocery/logout.html")


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category')


class ProductListView(ListView):
    model = Product
    template_name = 'grocery/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('category_detail')

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={'category_id': self.kwargs['category_id']})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('category_detail')

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={'category_id': self.kwargs['category_id']})


class ProductDeleteView(DeleteView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={'category_id': self.kwargs['category_id']})


# class CartView(DeleteView):
#     model = Cart
#     template_name = 'grocery/cart.html'
#     context_object_name = 'cart'
#
#     def get_form_kwargs(self, **kwargs):
#         kwargs = super().get_form_kwargs()
#         cart_id = Cart.objects.get_or_create(user_id=self.request.user.pk)
#         kwargs['pk'] = cart_id
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

def cart_view(request):
    cart = None
    cart_items = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cart_items.all()

    context = {"cart": cart, "cart_items": cart_items}
    return render(request, "grocery/cart.html", context)


def add_to_cart(request):
    data = request.POST.copy()
    product_id = data.get("id")
    product = Product.objects.get(id=product_id)
    category_from_product = Product.objects.all().filter(id=product_id).values('category_id')
    for catetegory_ids in category_from_product:
        category_id = catetegory_ids['category_id']

    if request.user.is_authenticated:

        cart, created_cart = Cart.objects.get_or_create(user=request.user)

        cart_item, created_cart_item = CartItem.objects.get_or_create(product=product, cart=cart)
        cart_item.count = int(cart_item.count or 0) + 1
        cart_item.save()

    # context = {"cart": cart, "category_id": category_id}
    return redirect('category_detail', category_id)


class MakeOrderView(CreateView):
    model = Cart
    form_class = OrderForm
    template_name = 'grocery/order_form.html'
    context_object_name = 'cart'
    success_url = reverse_lazy('submit_order')

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        Order.objects.create(user=request.user, address=data["address"])
        cart = Cart.objects.all().filter(user_id=request.user.pk)
        cart.delete()
        return render(request, 'grocery/confirm_order.html')

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class OrderPaymentView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'grocery/confirm_order.html'
