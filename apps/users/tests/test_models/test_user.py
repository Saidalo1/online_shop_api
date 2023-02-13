from itertools import cycle
from random import shuffle, seed

import pytest
from django.db import IntegrityError
from faker import Faker
from faker.providers.person.en import Provider
from model_bakery import baker

from users.models import User


@pytest.mark.django_db
class TestUserView:

    @pytest.fixture
    def faker(self):
        faker = Faker()
        return faker

    @pytest.fixture
    def user(self, faker):
        return baker.make(User, username=faker.user_name(), email=faker.email(), password=faker.password())

    @pytest.fixture
    def users(self, faker):
        first_names = list(set(Provider.first_names[:10]))
        seed(4321)
        shuffle(first_names)
        return baker.make(User, _quantity=10, username=cycle(first_names), email=faker.email(),
                          is_active=True)

    def test_create_user_model(self, users, faker):
        user = User.objects.create(username='User0001', email='user@gmail.com', password=faker.password(),
                                   is_active=True)
        count = User.objects.count()
        assert count == 11
        assert user.username == 'User0001'
        assert user.email == 'user@gmail.com'

        # wrong test
        try:
            User.objects.create(username=None, email=None, password=None)
            assert False
        except IntegrityError:
            assert True

    def test_update_user_model(self, user):
        username = 'NEW NAME'
        user.username = username
        user.save()
        assert user.username == username

        # wrong test
        try:
            user.username = None
            user.email = None
            user.password = None
            user.save()
            assert False
        except IntegrityError:
            assert True

    def test_delete_user_model(self, user):
        old_count = User.objects.count()
        assert old_count == 1
        user.delete()
        new_count = User.objects.count()
        assert new_count == 0
