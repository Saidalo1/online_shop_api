import pytest
from django.core import mail
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode
from faker import Faker
from faker_commerce import Provider
from jwt.utils import force_bytes
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

from users.models import User
from users.utils.tokens import account_activation_token


@pytest.mark.django_db
class TestCategoryAPIView:

    @pytest.fixture
    def fake(self):
        fake = Faker()
        fake.add_provider(Provider)
        return fake

    @pytest.fixture
    def register_user(self, fake, client):
        url = reverse_lazy('register')
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        data = {
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': password
        }
        response = client.post(url, data)
        assert response.status_code == HTTP_201_CREATED
        assert response.data['message'] == 'Check your email'
        assert len(response.data) == 1
        assert len(mail.outbox) == 1

        user = User.objects.get(username=username, email=email)
        assert user.is_active is False
        activation_url = reverse('activate_user',
                                 kwargs={'uidb64': urlsafe_base64_encode(force_bytes(str(user.pk))),
                                         'token': account_activation_token.make_token(user)})
        response = client.get(activation_url)
        user = User.objects.get(username=username, email=email)
        assert response.status_code == HTTP_200_OK
        assert user.username == username
        assert user.email == email
        assert user.is_active is True
        return user, password

    @pytest.fixture
    def login_access(self, register_user, client):
        url = reverse_lazy('token_obtain_pair')
        data = {'username': register_user[0],
                'password': register_user[1]}
        response = client.post(url, data)
        assert response.status_code == HTTP_200_OK
        return response.data['access']

    def test_category_api(self, client, login_access):
        url = reverse_lazy('category-list')
        response = client.get(url, headers={'Authorization': f'Bearer {login_access}'})
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 0
