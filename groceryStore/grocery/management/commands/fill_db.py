from django.core.management.base import BaseCommand
from grocery.models import Category, Product


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        Category.objects.all().delete()

        meat_category = Category.objects.create(name='Meat',
                                                picture='https://images.unsplash.com/photo-1595356161904-6708c97be89c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',
                                                )
        meat_category.save()

        fruit_category = Category.objects.create(name='Fruits',
                                                 picture='https://images.unsplash.com/photo-1610832958506-aa56368176cf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
                                                 )
        fruit_category.save()

        vegetables_category = Category.objects.create(name='Vegetables',
                                                      picture='https://media.istockphoto.com/id/533209791/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BF%D0%BB%D0%B5%D1%82%D0%B5%D0%BD%D0%B0%D1%8F-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B0-%D1%81-%D1%80%D0%B0%D0%B7%D0%BB%D0%B8%D1%87%D0%BD%D1%8B%D0%BC%D0%B8-%D1%81%D1%8B%D1%80%D0%BE%D0%B9-%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5-%D0%BE%D0%B2%D0%BE%D1%89%D0%B8-%D0%B2-%D1%81%D0%B0%D0%B4%D1%83.jpg?s=612x612&w=0&k=20&c=1xkv1094cLwLJMtN0PEPTyEpHFCphr7WHE-05eGi098=',
                                                      )
        vegetables_category.save()

        drink_category = Category.objects.create(name='Drinks',
                                                 picture='https://images.unsplash.com/photo-1656936611703-a1ede070073c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
                                                 )
        drink_category.save()

        pork = Product.objects.create(name='Pork',
                                      category=meat_category,
                                      price='450',
                                      units='rub/kg',
                                      composition='100% pork',
                                      picture='https://images.unsplash.com/photo-1602470521006-aaea8b2fcc36?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
                                      desc='Pork is classified a red meat because it contains more myoglobin than chicken or fish. When fresh pork is cooked, it becomes lighter in color, but it is still a red meat. Pork is classed as "livestock" along with veal, lamb, and beef. All livestock are considered red meat.',
                                      )
        pork.save()

        chicken = Product.objects.create(name='Chicken',
                                          category=meat_category,
                                          price='290',
                                          units='rub/kg',
                                          composition='100% chicken',
                                          picture='https://media.istockphoto.com/id/1330024022/photo/boneless-raw-chicken-thigh-fillet-wooden-background-top-view.jpg?b=1&s=170667a&w=0&k=20&c=Omv-gND2l_4JO0NaMfpt6uEQnjcUxB5580y70NqGqSs=',
                                          desc='Chicken meat is considered as an easily available source of high-quality protein and other nutrients that are necessary for proper body functioning. ')
        chicken.save()

        red_apple = Product.objects.create(name='Red apple',
                                           category=fruit_category,
                                           price='290',
                                           units='rub/kg',
                                           composition='100% apple',
                                           picture='https://images.unsplash.com/photo-1439127989242-c3749a012eac?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8cmVkJTIwYXBwbGV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
                                           desc='Red Delicious apples are medium-sized and have a conical shape.')

        red_apple.save()

        golden_apple = Product.objects.create(name='Golden apple',
                                              category=fruit_category,
                                              price='240',
                                              units='rub/kg',
                                              composition='100% apple',
                                              picture='https://images.unsplash.com/photo-1414396914239-e70522479d13?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Z29sZGVuJTIwYXBwbGV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
                                              desc='Golden Delicious is a large, yellowish-green skinned cultivar and very sweet to the taste. It is prone to bruising and shriveling, so it needs careful handling and storage. It is a favorite for salads, apple sauce, and apple butter.')

        golden_apple.save()

        potato = Product.objects.create(name='Potato',
                                        category=vegetables_category,
                                        price='40',
                                        units='rub/kg',
                                        composition='100% potato',
                                        picture='https://images.unsplash.com/photo-1518977676601-b53f82aba655?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80')
        potato.save()

        pepsi = Product.objects.create(name='Pepsi',
                                       category=drink_category,
                                       price='120',
                                       units='rub/kg',
                                       composition='Carbonated Water, Sugar, Colour (Caramel E150d), Acid (Phosphoric Acid), Flavourings (including Caffeine)',
                                       picture='https://images.unsplash.com/photo-1546695259-ad30ff3fd643?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1331&q=80')
        pepsi.save()
