import random
from itertools import cycle

import pytest
from django.db.utils import IntegrityError
from faker import Faker
from faker_commerce import PRODUCT_DATA, Provider
from model_bakery import baker

from orders.models import Product, Category, SubCategory, ProductRating
from users.models import User


@pytest.mark.django_db
class TestProductRatingView:

    @pytest.fixture
    def fake(self):
        fake = Faker()
        fake.add_provider(Provider)
        return fake

    @pytest.fixture
    def categories(self):
        fake = Faker()
        return baker.make(Category, _quantity=10, name=fake.text()[:50])

    @pytest.fixture
    def sub_category(self, categories, fake):
        return baker.make(SubCategory, name=fake.text()[:50], category=fake.random.choice(categories))

    @pytest.fixture
    def sub_categories(self, fake):
        categories = baker.make(Category, _quantity=10, name=fake.text()[:50])
        return baker.make(SubCategory, _quantity=10, name=fake.text()[:50], category=cycle(categories))

    @pytest.fixture
    def product(self, sub_category, fake):
        return baker.make(Product, name=random.choice(PRODUCT_DATA['product']),
                          description=fake.paragraph(nb_sentences=15),
                          count=fake.pyint(), price=fake.ecommerce_price(),
                          image=fake.file_path(category='image'),
                          category=sub_category, details=fake.pydict(), sale_percent=fake.random_int(0, 100))

    @pytest.fixture
    def products(self, sub_categories, fake):
        return baker.make(Product, name=cycle(PRODUCT_DATA['product']), description=fake.paragraph(nb_sentences=15),
                          count=fake.pyint(), price=fake.ecommerce_price(),
                          image=fake.file_path(category='image'),
                          category=cycle(sub_categories), details=fake.pydict(), sale_percent=fake.random_int(0, 100),
                          _quantity=10)

    @pytest.fixture
    def user(self, fake):
        return baker.make(User, email=fake.unique.ascii_free_email(), password=fake.password(), is_active=True)

    @pytest.fixture
    def product_rating(self, product, fake, user):
        return baker.make(ProductRating, product=product, rating=fake.random_int(0, 5), user=user)

    @pytest.fixture
    def product_ratings(self, products, fake, user):
        return baker.make(ProductRating, _quantity=10, product=cycle(products), rating=fake.random_int(0, 5), user=user)

    def test_create_product_rating_model(self, product, product_ratings, user):
        assert ProductRating.objects.count() == 10
        product_rating = ProductRating.objects.create(product=product, rating=5, user=user)
        count = ProductRating.objects.count()
        assert count == 11
        assert product_rating.product == product
        assert product_rating.rating == 5
        assert product_rating.user == user

        # wrong test
        try:
            ProductRating.objects.create(product=None, rating=None, user=None)
            assert False
        except IntegrityError:
            assert True

    def test_update_product_rating_model(self, product_rating, product, user):
        product_rating.product = product
        product_rating.rating = 4
        product_rating.user = user
        product_rating.save()
        assert product_rating.product == product
        assert product_rating.rating == 4
        assert product_rating.user == user

        # wrong test
        try:
            product_rating.product = None
            product_rating.rating = None
            product_rating.user = None
            product_rating.save()
            assert False
        except IntegrityError:
            assert True

    def test_delete_product_rating_model(self, product_rating):
        old_count = ProductRating.objects.count()
        assert old_count == 1
        product_rating.delete()
        new_count = ProductRating.objects.count()
        assert new_count == 0
