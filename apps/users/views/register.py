from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from root.settings import EMAIL_HOST_USER
from users.models import User
from users.serializers import UserCreateModelSerializer
from users.utils.tokens import account_activation_token


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer
    permission_classes = (~IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        created = super().create(request, *args, **kwargs)
        user = User.objects.get(id=created.data['id'])
        message = render_to_string('activation.html', {
            'username': user.username,
            'domain': get_current_site(request),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail('Activation Link', message, EMAIL_HOST_USER, [created.data['email']])
        return Response({'message': 'Check your email'}, status.HTTP_201_CREATED)
