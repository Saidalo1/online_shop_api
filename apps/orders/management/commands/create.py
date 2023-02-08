from itertools import cycle

from django.core.management.base import BaseCommand
from faker import Faker
from faker_commerce import Provider, CATEGORIES, PRODUCT_DATA
from model_bakery import baker

from orders.models import Category, SubCategory


class Command(BaseCommand):
    help = 'Create random categories'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        # get quantity
        total = kwargs['total']

        # faker to create data
        fake = Faker()

        # add provider
        fake.add_provider(Provider)

        # fake seed
        Faker.seed(0)

        # get categories
        sub_categories = SubCategory.objects.all()
        categories = Category.objects.all()

        if categories.count() < 22:
            # add categories
            baker.make('orders.Category', name=cycle(CATEGORIES), _quantity=22)
            categories = Category.objects.all()

        if sub_categories.count() < 22:
            # add subcategories
            baker.make('orders.SubCategory', name=cycle(CATEGORIES), category=cycle(categories), _quantity=22)
            sub_categories = SubCategory.objects.all()

        # add products
        baker.make('orders.Product', name=cycle(PRODUCT_DATA['product']), description=fake.paragraph(nb_sentences=15),
                   count=fake.pyint(), price=fake.ecommerce_price(),
                   image=fake.file_path(depth=total, category='image'),
                   category=cycle(sub_categories), details=fake.pydict(), sale_percent=fake.random_int(0, 100),
                   _quantity=total)
