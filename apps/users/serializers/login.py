from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.serializers.userInfo import GetMeModelSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['data'] = GetMeModelSerializer(self.user).data
        return data
