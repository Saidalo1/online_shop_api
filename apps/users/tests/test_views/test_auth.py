import pytest
from django.core import mail
from django.utils.http import urlsafe_base64_encode
from faker import Faker
from faker_commerce import Provider
from jwt.utils import force_bytes
from rest_framework.exceptions import ErrorDetail
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST

from users.models import User
from users.utils.tokens import account_activation_token


@pytest.mark.django_db
class TestAuthAPIView:

    @pytest.fixture
    def fake(self):
        fake = Faker()
        fake.add_provider(Provider)
        return fake

    @pytest.fixture
    def test_register_api(self, fake, client):
        url = reverse('register')
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

        # wrong test

        # empty field
        response = client.post(url)
        assert response.status_code == HTTP_400_BAD_REQUEST
        required_field_error = [ErrorDetail(string='This field is required.', code='required')]
        assert response.data['username'] == required_field_error
        assert response.data['email'] == required_field_error
        assert response.data['password'] == required_field_error
        assert response.data['confirm_password'] == required_field_error
        assert len(response.data) == 4
        assert len(mail.outbox) == 1

        # incorrect field
        data = {
            'username': 'a',
            'email': 'test_email.com',
            'password': '123321',
            'confirm_password': '123321'
        }
        response = client.post(url, data)
        assert response.status_code == HTTP_400_BAD_REQUEST
        assert len(response.data) == 2
        assert response.data['email'] == [ErrorDetail(string='Enter a valid email address.', code='invalid')]
        assert response.data['password'] == [ErrorDetail(string='Password is too short.', code='invalid')]
        data = {
            'username': fake.user_name(),
            'email': fake.email(),
            'password': '123098AS',
            'confirm_password': '123098ASD'
        }
        response = client.post(url, data)
        assert response.status_code == HTTP_400_BAD_REQUEST
        assert len(response.data) == 1
        assert response.data['non_field_errors'] == [ErrorDetail(string="Passwords didn't match.", code='invalid')]
        return {"username": username, "email": email, "password": password}

    def test_login_api(self, test_register_api, client):
        url = reverse('token_obtain_pair')
        response = client.post(url, test_register_api)
        assert response.status_code == HTTP_200_OK
        assert response.data['access'] and response.data['refresh']
        assert response.data['data']['username'] == test_register_api.get('username')
        assert response.data['data']['email'] == test_register_api.get('email')
        assert len(response.data) == 3

        # wrong test

        # empty field
        response = client.post(url)
        print(response.data)
        required_field_error = [ErrorDetail(string='This field is required.', code='required')]
        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['username'] == required_field_error
        assert response.data['password'] == required_field_error
        assert len(response.data) == 2
