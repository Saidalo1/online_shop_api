import random

import pytest
from django.db.utils import IntegrityError
from faker import Faker
from faker_commerce import PRODUCT_DATA, Provider
from model_bakery import baker

from orders.models import Product, Category, SubCategory, ProductImages


@pytest.mark.django_db
class TestProductImagesView:

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
    def sub_category(self, categories):
        fake = Faker()
        return baker.make(SubCategory, name=fake.text()[:50], category=fake.random.choice(categories))

    @pytest.fixture
    def product(self, sub_category, fake):
        return baker.make(Product, name=random.choice(PRODUCT_DATA['product']),
                          description=fake.paragraph(nb_sentences=15),
                          count=fake.pyint(), price=fake.ecommerce_price(),
                          image=fake.file_path(category='image'),
                          category=sub_category, details=fake.pydict(), sale_percent=fake.random_int(0, 100))

    @pytest.fixture
    def product_image(self, product, fake):
        return baker.make(ProductImages, product=product, image=fake.file_path(category='image'))

    @pytest.fixture
    def product_images(self, product, fake):
        return baker.make(ProductImages, _quantity=10, product=product, image=fake.file_path(category='image'))

    def test_create_product_image_model(self, product, product_images):
        assert ProductImages.objects.count() == 10
        product_image = ProductImages.objects.create(product=product, image='/product/images/1.jpg')
        count = ProductImages.objects.count()
        assert count == 11
        assert product_image.product == product
        assert product_image.image == '/product/images/1.jpg'

        # wrong test
        try:
            ProductImages.objects.create(product=None, image=None)
            assert False
        except IntegrityError:
            assert True

    def test_update_product_image_model(self, product_image, product):
        product_image.product = product
        product_image.image = '/products/image/2.jpg'
        product_image.save()
        assert product_image.product == product
        assert product_image.image == '/products/image/2.jpg'

        # wrong test
        try:
            product_image.product = None
            product_image.image = None
            product_image.save()
            assert False
        except IntegrityError:
            assert True

    def test_delete_product_image_model(self, product_image):
        old_count = ProductImages.objects.count()
        assert old_count == 1
        product_image.delete()
        new_count = ProductImages.objects.count()
        assert new_count == 0
