import uuid

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500, blank=True)
    composition = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    units = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='img', default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.price} {self.desc} {self.composition} {self.picture} {self.units}'



