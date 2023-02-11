from django.core.management.base import BaseCommand, CommandError
from grocery.models import Category


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        Category.objects.all().delete()

        meat_category = Category.objects.create(name='Meat')
        meat_category.save()

        fruit_category = Category.objects.create(name='Fruits')
        fruit_category.save()

        vegetables_category = Category.objects.create(name='Vegetables')
        vegetables_category.save()

        drink_category = Category.objects.create(name='Drinks')
        drink_category.save()
