from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from users.models import User
from users.utils.tokens import account_activation_token


class ActivateUserApiView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'User is activated'})
        return Response({'message': 'invalid link'}, HTTP_404_NOT_FOUND)
