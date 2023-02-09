import random
from itertools import cycle

import pytest
from django.db.utils import IntegrityError
from faker import Faker
from faker_commerce import PRODUCT_DATA, Provider
from model_bakery import baker

from orders.models import Product, SubCategory, Category


@pytest.mark.django_db
class TestProductView:

    @pytest.fixture
    def categories(self):
        fake = Faker()
        return baker.make(Category, _quantity=10, name=fake.text()[:50])

    @pytest.fixture
    def sub_category(self, categories):
        fake = Faker()
        return baker.make(SubCategory, name=fake.text()[:50], category=cycle(categories))

    @pytest.fixture
    def sub_categories(self, categories):
        fake = Faker()
        return baker.make(SubCategory, _quantity=10, name=fake.text()[:50], category=cycle(categories))

    @pytest.fixture
    def product(self, sub_categories):
        fake = Faker()
        fake.add_provider(Provider)
        return baker.make(Product, name=random.choice(PRODUCT_DATA['product']), description=fake.paragraph(nb_sentences=15),
                   count=fake.pyint(), price=fake.ecommerce_price(),
                   image=fake.file_path(category='image'),
                   category=cycle(sub_categories), details=fake.pydict(), sale_percent=fake.random_int(0, 100))

    @pytest.fixture
    def products(self, sub_categories):
        fake = Faker()
        fake.add_provider(Provider)
        return baker.make(Product, name=cycle(PRODUCT_DATA['product']), description=fake.paragraph(nb_sentences=15),
                   count=fake.pyint(), price=fake.ecommerce_price(),
                   image=fake.file_path(category='image'),
                   category=cycle(sub_categories), details=fake.pydict(), sale_percent=fake.random_int(0, 100),
                   _quantity=10)

    def test_create_product_model(self, products, sub_category):
        product = Product.objects.create(name='New Product', category=sub_category)
        count = Product.objects.count()
        assert count == 11
        assert product.name == 'New Product'

        # wrong test
        try:
            Product.objects.create(name=None, description=None, count=None, price=None, image=None, category=None,
                                   details=None, sale_percent=None)
            assert False
        except IntegrityError:
            assert True

    def test_update_product_model(self, sub_categories, product):
        fake = Faker()
        fake.add_provider(Provider)
        name = 'NEW NAME'
        description = 'NEW DESCRIPTION'
        count = 50
        price = 150000.01
        image = fake.file_path(category='image')
        category = random.choice(sub_categories)
        details = {"ghz": "5.5"}
        sale_percent = 5
        product.name = '1'
        product.save()
        assert product.name == '1'
        product = Product(name=name, description=description, count=count, price=price, image=image, category=category,
                          details=details, sale_percent=sale_percent)
        product.save()
        assert product.name == name
        assert product.description == description
        assert product.count == count
        assert product.price == price
        assert product.image == image
        assert product.category == category
        assert product.details == details
        assert product.sale_percent == sale_percent

        # wrong test
        try:
            product.name = None
            product.save()
            assert False
        except IntegrityError:
            assert True

    def test_delete_product_model(self, product):
        old_count = Product.objects.count()
        assert old_count == 1
        product.delete()
        new_count = Product.objects.count()
        assert new_count == 0
