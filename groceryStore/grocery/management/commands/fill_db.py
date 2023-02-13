from django.core.management.base import BaseCommand
from grocery.models import Category, Product


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

        pork = Product.objects.create(name='Pork',
                                      category=meat_category,
                                      price='450',
                                      units='rub/kg',
                                      composition='100% pork',
                                      desc='Pork is classified a red meat because it contains more myoglobin than chicken or fish. When fresh pork is cooked, it becomes lighter in color, but it is still a red meat. Pork is classed as "livestock" along with veal, lamb, and beef. All livestock are considered red meat.')
        pork.save()

        chicken = Product.objects.create(name='Chicken',
                                      category=meat_category,
                                      price='290',
                                      units='rub/kg',
                                      composition='100% chicken',
                                      desc='Chicken meat is considered as an easily available source of high-quality protein and other nutrients that are necessary for proper body functioning. ')
        chicken.save()

        red_apple = Product.objects.create(name='Red apple',
                                      category=fruit_category,
                                      price='290',
                                      units='rub/kg',
                                      composition='100% apple',
                                      desc='Red Delicious apples are medium-sized and have a conical shape.')
        red_apple.save()

        golden_apple = Product.objects.create(name='Golden apple',
                                      category=fruit_category,
                                      price='240',
                                      units='rub/kg',
                                      composition='100% apple',
                                      desc='Golden Delicious is a large, yellowish-green skinned cultivar and very sweet to the taste. It is prone to bruising and shriveling, so it needs careful handling and storage. It is a favorite for salads, apple sauce, and apple butter.')

        golden_apple.save()
