from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from grocery.forms import RegisterForm, CategoryForm, ProductForm
import django_filters
from .models import Category, Product


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


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category']


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["category"] = get_object_or_404(Category, id=self.kwargs['category_id'])
    #     return context

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
