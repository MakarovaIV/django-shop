from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from grocery.forms import RegisterForm, CategoryForm, ProductForm, MakeOrderForm, OrderForm
from .models import Category, Product, Cart, CartItem, Order


class CategoryListView(ListView):
    model = Category
    template_name = 'grocery/category/category_list.html'
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
    template_name = 'grocery/product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, id=self.kwargs['category_id'])

        if self.request.user.is_authenticated:
            cart = Cart.objects.filter(user=self.request.user).last()
            if cart:
                cart_items = CartItem.objects.filter(cart_id=cart.id).values('count', 'product_id')
                map = {}
                for cart_item in cart_items:
                    map[str(cart_item['product_id'])] = cart_item['count']

                for product in context['products']:
                    if str(product.pk) in map:
                        product.count_in_cart = map[str(product.pk)]

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

    if request.user.is_authenticated:
        cart, created_cart = Cart.objects.get_or_create(user=request.user)

        cart_item, created_cart_item = CartItem.objects.get_or_create(product=product, cart=cart)
        current_count = int(cart_item.count or 0)

        new_count = current_count
        if data.get("btn_func") == "decrement":
            new_count = current_count - 1
        elif data.get("btn_func") == "increment":
            new_count = current_count + 1
        else:
            new_count = 1

        if new_count <= 0:
            cart_item.delete()
            print("ZCzc")
        else:
            cart_item.count = new_count
            cart_item.save()

    return redirect(data['current_path'])


class MakeOrderView(CreateView):
    model = Cart
    form_class = MakeOrderForm
    template_name = 'grocery/order/order_form.html'
    context_object_name = 'cart'
    success_url = reverse_lazy('submit_order')

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        order = Order.objects.create(user=request.user, address=data["address"])
        cart_id = Cart.objects.filter(user_id=request.user.pk).first()
        print("cart:", cart_id)

        order_items = CartItem.objects.filter(cart_id=cart_id)
        print("order_items:", order_items)
        for order_item in order_items:
            order_item.order_id = order.id
            order_item.save()

        cart_id.delete()
        return render(request, 'grocery/order/confirm_order.html')

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class OrderPaymentView(CreateView):
    model = Order
    form_class = MakeOrderForm
    template_name = 'grocery/order/confirm_order.html'


class OrderListView(ListView):
    model = Order
    form_class = OrderForm
    template_name = 'grocery/order/order_list.html'
    context_object_name = 'orderlist'

    @staticmethod
    def format_product(product):
        formatted_text = product['name'] + ' (' + str(product['price']) + ' ' + product['units'] + ')'
        product['formatted_text'] = formatted_text
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(user_id=self.request.user.pk)
        for order in orders:
            product_ids = order.order_items.all().values('product')
            products = Product.objects.filter(id__in=product_ids)

            product_list = products.values('name', 'price', 'units', 'picture')
            order.product_list = list(map(self.format_product, product_list))

        context["custom_orders"] = orders
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'grocery/product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        temp = Product.objects.filter(id=self.kwargs['pk']).values('category_id').last()
        context['category_id'] = temp['category_id']

        if self.request.user.is_authenticated:
            cart = Cart.objects.filter(user=self.request.user).last()
            if cart:
                cart_item = CartItem.objects.filter(cart_id=cart.id, product_id=context['product'].pk).values('count').last()

                if cart_item:
                    context['count_in_cart'] = cart_item['count']

        return context
