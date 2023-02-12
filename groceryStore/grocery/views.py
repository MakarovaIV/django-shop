from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from grocery.forms import RegisterForm, CategoryForm
from .models import Category


def main_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'grocery/index.html',  context=context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login/")

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
                return redirect("main")
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
    success_url = reverse_lazy('main')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('main')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('main')
