from rest_framework.serializers import ModelSerializer

from users.models import User


class GetMeModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')
