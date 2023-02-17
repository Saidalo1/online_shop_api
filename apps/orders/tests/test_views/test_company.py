import pytest
from django.urls import reverse
from faker import Faker
from faker_commerce import Provider
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK

from orders.models import Company


@pytest.mark.django_db
class TestCompanyAPIView:

    @pytest.fixture
    def fake(self):
        fake = Faker()
        fake.add_provider(Provider)
        return fake

    @pytest.fixture
    def companies(self):
        return baker.make(Company, 15)

    def test_company_list_api(self, client, companies):
        url = reverse('company-list')
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == len(companies) == 15 == Company.objects.count()
        for item1, item2 in zip(companies, response.data):
            assert item1.id == item2['id']
            assert item1.name == item2['name']

    def test_company_detail_api(self, client, fake, companies):
        random_company = fake.random.choice(companies)
        url = reverse('company-detail', (random_company.id,))
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 4
        assert response.data['id'] == random_company.id
        assert response.data['name'] == random_company.name
