import random
from itertools import cycle

import pytest
from django.db.utils import IntegrityError
from faker import Faker
from faker_commerce import PRODUCT_DATA, Provider
from model_bakery import baker

from orders.models import Product, Category, SubCategory, ProductComment
from users.models import User


@pytest.mark.django_db
class TestProductCommentsView:

    @pytest.fixture
    def fake(self):
        fake = Faker()
        fake.add_provider(Provider)
        return fake

    @pytest.fixture
    def category(self, fake):
        return baker.make(Category, name=fake.text()[:50])

    @pytest.fixture
    def categories(self, fake):
        return baker.make(Category, _quantity=10, name=fake.text()[:50])

    @pytest.fixture
    def sub_category(self, category, fake):
        return baker.make(SubCategory, name=fake.text()[:50], category=category)

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
    def product_comment(self, product, fake, user):
        return baker.make(ProductComment, product=product, title=fake.text()[:250], text=fake.text()[:1500], user=user,
                          is_active=True)

    @pytest.fixture
    def product_comments(self, products, fake, user):
        return baker.make(ProductComment, _quantity=10, product=cycle(products), title=fake.text()[:250],
                          text=fake.text()[:1500], user=user,
                          is_active=True)

    def test_create_product_comment_model(self, fake, product, product_comments, user):
        assert ProductComment.objects.count() == 10
        title = fake.text()[:250]
        text = fake.text()[:1500]
        product_comment = baker.make(ProductComment, product=product, title=title, text=text, user=user,
                                     is_active=True)
        count = ProductComment.objects.count()
        assert count == 11
        assert product_comment.product == product
        assert product_comment.text == text
        assert product_comment.title == title
        assert product_comment.user == user
        assert product_comment.is_active is True

        # is active False
        baker.make(ProductComment, product=product, title=title, text=text, user=user, is_active=False)
        count = ProductComment.objects.filter(is_active=True).count()
        assert count == 11

        # wrong test
        try:
            ProductComment.objects.create(product=None, title=None, text=None, user=None, is_active=None)
            assert False
        except IntegrityError:
            assert True

    def test_update_product_comment_model(self, product_comment, product, user):
        product_comment.title = 'Product Comment'
        product_comment.product = product
        product_comment.text = 'New product'
        product_comment.user = user
        product_comment.save()
        assert product_comment.title == 'Product Comment'
        assert product_comment.product == product
        assert product_comment.text == 'New product'
        assert product_comment.user == user

        # wrong test
        try:
            product_comment.product = None
            product_comment.title = None
            product_comment.text = None
            product_comment.user = None
            product_comment.is_active = None
            product_comment.save()
            assert False
        except IntegrityError:
            assert True

    def test_delete_product_comment_model(self, product_comment):
        old_count = ProductComment.objects.count()
        assert old_count == 1
        product_comment.delete()
        new_count = ProductComment.objects.count()
        assert new_count == 0
