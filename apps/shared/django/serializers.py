from rest_framework.serializers import ModelSerializer

from users.models import User


class GetUserNameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
