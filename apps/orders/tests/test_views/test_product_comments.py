import random
from itertools import cycle

import pytest
from django.core import mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from faker import Faker
from faker_commerce import Provider, PRODUCT_DATA
from jwt.utils import force_bytes
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from orders.models import SubCategory, Category, ProductComment, Product
from users.models import User
from users.utils.tokens import account_activation_token


@pytest.mark.django_db
class TestProductCommentAPIView:

    @pytest.fixture
    def fake(self):
        fake = Faker()
        fake.add_provider(Provider)
        return fake

    @pytest.fixture
    def categories(self, fake):
        return baker.make(Category, _quantity=10, name=fake.text()[:50])

    @pytest.fixture
    def sub_categories(self, fake, categories):
        return baker.make(SubCategory, _quantity=10, name=fake.text()[:50], category=cycle(categories))

    @pytest.fixture
    def products(self, sub_categories, fake):
        return baker.make(Product, name=cycle(PRODUCT_DATA['product']), description=fake.paragraph(nb_sentences=15),
                          count=fake.pyint(), price=fake.ecommerce_price(),
                          image=fake.file_path(category='image'),
                          category=cycle(sub_categories), details=fake.pydict(), sale_percent=fake.random_int(0, 100),
                          _quantity=10)

    @pytest.fixture
    def users(self, fake):
        counter = 0
        emails = set()
        while counter < 10:
            emails.add(fake.unique.ascii_free_email())
            counter += 1
        return baker.make(User, 10, email=cycle(emails), password=fake.password(), is_active=True)

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
        return {"username": username, "email": email, "password": password}

    @pytest.fixture
    def test_login_api(self, test_register_api, client):
        url = reverse('token_obtain_pair')
        response = client.post(url, test_register_api)
        assert response.status_code == HTTP_200_OK
        assert response.data['access'] and response.data['refresh']
        assert response.data['data']['username'] == test_register_api.get('username')
        assert response.data['data']['email'] == test_register_api.get('email')
        assert len(response.data) == 3
        return response.data['access']

    @pytest.fixture
    def product_comments(self, fake, products, users):
        return baker.make(ProductComment, _quantity=10, product=cycle(products), title=fake.text()[:250],
                          text=fake.text()[:1500], user=cycle(users), is_active=True)

    def test_product_comments_list_api(self, client, fake, product_comments, products, test_login_api):
        random_product = random.choice(products)
        url = reverse('comments-list', (random_product.id,))
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 1 == ProductComment.objects.filter(product_id=random_product.id).count()

        # wrong test
        url = reverse('comments-list', (100,))
        response = client.get(url)
        assert response.status_code == HTTP_404_NOT_FOUND
        assert len(response.data) == 1
        assert response.data['detail'] == f'Product with 100-id is not found'

    def test_product_detail_api(self, client, fake, product_comments, products):
        random_product = fake.random.choice(products)
        random_comment = fake.random.choice(ProductComment.objects.filter(product_id=random_product.id))
        url = reverse('comments-detail', (random_product.id, random_comment.id))
        response = client.get(url)
        print(response.data)
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 11
