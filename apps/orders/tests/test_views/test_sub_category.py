from itertools import cycle

import pytest
from django.urls import reverse
from faker import Faker
from faker_commerce import Provider
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK

from orders.models import SubCategory, Category


@pytest.mark.django_db
class TestSubCategoryAPIView:

    @pytest.fixture
    def fake(self):
        fake = Faker()
        fake.add_provider(Provider)
        return fake

    @pytest.fixture
    def categories(self):
        return baker.make(Category, 15)

    @pytest.fixture
    def sub_categories(self, categories):
        return baker.make(SubCategory, 15, category=cycle(categories))

    def test_category_list_api(self, client, sub_categories):
        url = reverse('sub_category-list')
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == len(sub_categories) == 15 == SubCategory.objects.count()
        for item1, item2 in zip(sub_categories, response.data):
            assert item1.id == item2['id']
            assert item1.name == item2['name']
            assert item1.category.id == item2['category']

    def test_category_detail_api(self, client, fake, sub_categories):
        random_sub_category = fake.random.choice(sub_categories)
        url = reverse('sub_category-detail', (random_sub_category.id,))
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 5
        assert response.data['id'] == random_sub_category.id
        assert response.data['name'] == random_sub_category.name
        assert response.data['category'] == random_sub_category.category.id
