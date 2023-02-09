import pytest
from django.db.utils import IntegrityError
from faker import Faker
from model_bakery import baker

from orders.models import Company


@pytest.mark.django_db
class TestCompanyView:

    @pytest.fixture
    def company(self):
        return baker.make(Company)

    @pytest.fixture
    def companies(self):
        faker = Faker()
        baker.make(Company, _quantity=10, name=faker.text()[:50])

    def test_create_company_model(self, companies):
        company = Company.objects.create(name='New Company')
        count = Company.objects.count()
        assert count == 11
        assert company.name == 'New Company'

        # wrong test
        try:
            Company.objects.create(name=None)
            assert False
        except IntegrityError:
            assert True

    def test_update_company_model(self, company):
        name = 'NEW NAME'
        company.name = name
        company.save()
        assert company.name == name

        # wrong test
        try:
            company.name = None
            company.save()
            assert False
        except IntegrityError:
            assert True

    def test_delete_company_model(self, company):
        old_count = Company.objects.count()
        assert old_count == 1
        company.delete()
        new_count = Company.objects.count()
        assert new_count == 0
