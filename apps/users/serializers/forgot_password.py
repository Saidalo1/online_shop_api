from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from users.models import User


class ForgotPasswordSerializer(Serializer):
    username = CharField(max_length=255)

    @staticmethod
    def validate_username(username):
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Username doesn't exists")
        return username
