import os

from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from orders.models import CentralProcessingUnit, VideoCard
from orders.serializers import CentralProcessingUnitModelSerializer
from root.settings import BASE_DIR
from shared.django import ReadOnly


class CentralProcessingUnitModelViewSet(ModelViewSet):
    queryset = CentralProcessingUnit.objects.all()
    serializer_class = CentralProcessingUnitModelSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAdminUser | ReadOnly,)

    def destroy(self, request, *args, **kwargs):
        if CentralProcessingUnit.objects.get(id=kwargs.get('pk')).image.url:
            image_url = CentralProcessingUnit.objects.get(id=kwargs.get('pk')).image.url
            os.remove(BASE_DIR + image_url)
        return super().destroy(request, *args, **kwargs)


class VideoCardModelViewSet(ModelViewSet):
    queryset = VideoCard.objects.all()
    serializer_class = CentralProcessingUnitModelSerializer
    parser_classes = (MultiPartParser,)

    def destroy(self, request, *args, **kwargs):
        if VideoCard.objects.get(id=kwargs.get('pk')).image.url:
            image_url = VideoCard.objects.get(id=kwargs.get('pk')).image.url
            os.remove(BASE_DIR + image_url)
        return super().destroy(request, *args, **kwargs)
