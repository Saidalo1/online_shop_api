from itertools import cycle

import pytest
from django.db.utils import IntegrityError
from faker import Faker
from model_bakery import baker

from orders.models import SubCategory, Category


@pytest.mark.django_db
class TestSubCategoryView:

    @pytest.fixture
    def category(self):
        return baker.make(Category)

    @pytest.fixture
    def sub_category(self):
        return baker.make(SubCategory)

    @pytest.fixture
    def sub_categories(self):
        faker = Faker()
        categories = baker.make(Category, _quantity=10, name=faker.text()[:50])
        baker.make(SubCategory, _quantity=10, name=faker.text()[:50], category=cycle(categories))

    def test_create_sub_category_model(self, sub_categories, category):
        sub_category = SubCategory.objects.create(name='New SubCategory', category=category)
        count = SubCategory.objects.count()
        assert count == 11
        assert sub_category.name == 'New SubCategory'

        # wrong test
        try:
            SubCategory.objects.create(name=None, category=category)
            assert False
        except IntegrityError:
            assert True

    def test_update_sub_category_model(self, sub_category):
        category = baker.make(Category)
        name = 'NEW NAME'
        sub_category.name = name
        sub_category.category = category
        sub_category.save()
        assert sub_category.name == name
        assert sub_category.category == category

        # wrong test
        try:
            sub_category.name = None
            sub_category.category = None
            sub_category.save()
            assert False
        except IntegrityError:
            assert True

    def test_delete_sub_category_model(self, sub_category):
        old_count = SubCategory.objects.count()
        assert old_count == 1
        sub_category.delete()
        new_count = SubCategory.objects.count()
        assert new_count == 0
