import pytest
from django.core import mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from faker import Faker
from faker_commerce import Provider
from rest_framework.reverse import reverse_lazy
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

from users.models import User


@pytest.mark.django_db
class TestAuthAPIView:

    @pytest.fixture
    def fake(self):
        fake = Faker()
        fake.add_provider(Provider)
        return fake

    def test_register_api(self, fake, client):
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

        for i in mail.outbox:
            token = i.body.split(' ')[-1]
            print(i.body)  # <-- the entire email body with the activation url
        token = token[38:-1]
        user = User.objects.get(email=email)
        user_id = urlsafe_base64_encode(force_bytes(user.pk))

        activation_url = reverse('activate_user', kwargs={'user_id': user_id, 'token': token})
        activation_url = 'http://127.0.0.1' + activation_url
        response = self.client.get(activation_url, follow=True)
        user = User.objects.get(email=email)

        assert response.status_code == HTTP_200_OK
        assert user.username == username
        assert user.email == email
        assert user.is_active is True
