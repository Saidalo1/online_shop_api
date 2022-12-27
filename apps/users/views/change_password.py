from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from users.serializers import ChangePasswordSerializer


class ChangePasswordApiView(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        return Response({'status': 'updated your password'})
