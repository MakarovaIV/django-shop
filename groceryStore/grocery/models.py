import uuid

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    picture = models.CharField(max_length=600)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500, blank=True)
    composition = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    units = models.CharField(max_length=10)
    picture = models.CharField(max_length=600)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.price} {self.desc} {self.composition} {self.picture} {self.units}'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        cart_items = self.cart_items.all()
        total = sum([(item.product.price * item.count) for item in cart_items])
        return total

    @property
    def total_count(self):
        cart_items = self.cart_items.all()
        count = sum([item.count for item in cart_items])
        return count


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    address = models.CharField(max_length=500)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.order_items} {self.address} {self.paid} {self.created}'

    @property
    def total_price(self):
        cart_items = self.order_items.all()
        total = sum([(item.product.price * item.count) for item in cart_items])
        return total

    @property
    def total_count(self):
        cart_items = self.order_items.all()
        count = sum([item.count for item in cart_items])
        return count


class CartItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product',
                                null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, related_name='cart_items', null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', null=True)
    count = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.product} {self.count} {self.cart}'



