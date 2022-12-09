from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserCreateModelSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer
