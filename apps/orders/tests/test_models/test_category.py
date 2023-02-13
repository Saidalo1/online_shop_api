import pytest
from django.db import IntegrityError
from faker import Faker
from model_bakery import baker

from orders.models import Category


@pytest.mark.django_db
class TestCategoryView:

    @pytest.fixture
    def faker(self):
        faker = Faker()
        return faker

    @pytest.fixture
    def category(self):
        return baker.make(Category)

    @pytest.fixture
    def categories(self, faker):
        return baker.make(Category, _quantity=10, name=faker.text()[:50])

    def test_create_category_model(self, categories):
        count = Category.objects.count()
        assert count == 10
        category = Category.objects.create(name='New Category')
        count = Category.objects.count()
        assert count == 11
        assert category.name == 'New Category'

        # wrong test
        try:
            Category.objects.create(name=None)
            assert False
        except IntegrityError:
            assert True

    def test_update_category_model(self, category):
        name = 'NEW NAME'
        category.name = name
        category.save()
        assert category.name == name

        # wrong test
        try:
            category.name = None
            category.save()
            assert False
        except IntegrityError:
            assert True

    def test_delete_category_model(self, category):
        old_count = Category.objects.count()
        assert old_count == 1
        category.delete()
        new_count = Category.objects.count()
        assert new_count == 0
