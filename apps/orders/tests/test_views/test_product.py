from itertools import cycle

import pytest
from django.urls import reverse
from faker import Faker
from faker_commerce import Provider, PRODUCT_DATA
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK

from orders.models import SubCategory, Category, Product


@pytest.mark.django_db
class TestProductAPIView:

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
    def sub_categories(self, categories):
        fake = Faker()
        return baker.make(SubCategory, _quantity=15, name=fake.text()[:50], category=cycle(categories))

    @pytest.fixture
    def products(self, sub_categories, fake):
        return baker.make(Product, name=cycle(PRODUCT_DATA['product']), description=fake.paragraph(nb_sentences=15),
                          count=fake.pyint(), price=fake.ecommerce_price(),
                          image=fake.file_path(category='image'),
                          category=cycle(sub_categories), details=fake.pydict(), sale_percent=fake.random_int(0, 100),
                          _quantity=15)

    def test_product_list_api(self, client, products):
        url = reverse('product-list')
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == len(products) == 15 == Product.objects.count()
        products = Product.objects.order_by('-created_at')
        for item1, item2 in zip(products, response.data):
            assert item1.id == item2['id']
            assert item1.name == item2['name']
            assert item1.category.id == item2['category']
            assert item1.description == item2['description']
            assert item1.views == item2['views']
            assert item1.count == item2['count']
            assert item1.price == item2['price']
            assert f'http://testserver{item1.image.url}' == item2['image']
            assert item1.details == item2['details']
            assert item1.sale_percent == item2['sale_percent']

    def test_product_detail_api(self, client, fake, products):
        random_product = fake.random.choice(products)
        url = reverse('product-detail', (random_product.id,))
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 11
        assert response.data['id'] == random_product.id
        assert response.data['name'] == random_product.name
        assert response.data['category'] == random_product.category.id
        assert response.data['description'] == random_product.description
        assert response.data['views'] == random_product.views + 1
        assert response.data['count'] == random_product.count
        assert response.data['price'] == random_product.price
        assert response.data['image'] == f'http://testserver{random_product.image.url}'
        assert response.data['sale_percent'] == random_product.sale_percent
