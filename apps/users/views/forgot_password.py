from django.core.mail import send_mail
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from root.settings import EMAIL_HOST_USER
from users.models import User
from users.serializers import ForgotPasswordSerializer


class ForgotPasswordApiView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ForgotPasswordSerializer

    def __send_email_confirmation_token(self, username):
        user = User.objects.filter(username=username).first()
        send_mail('Reset password', 'For reset password click here', EMAIL_HOST_USER, [user.email])

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        username = serializer_data.data.get('username')
        self.__send_email_confirmation_token(username)
        return Response({'status': 'check your email'})
