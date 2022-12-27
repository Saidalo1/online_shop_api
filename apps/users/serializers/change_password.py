from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from users.models import User


class ChangePasswordSerializer(Serializer):
    token = CharField(max_length=255)
    password = CharField(max_length=255)
    confirm_password = CharField(max_length=255)

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Username doesn't exists")
        return username
