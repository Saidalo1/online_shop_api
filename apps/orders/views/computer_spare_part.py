from orders.models import CentralProcessingUnit, VideoCard
from orders.serializers import CentralProcessingUnitModelSerializer
from rest_framework.viewsets import ModelViewSet


class CentralProcessingUnitModelViewSet(ModelViewSet):
    queryset = CentralProcessingUnit.objects.all()
    serializer_class = CentralProcessingUnitModelSerializer


class VideoCardModelViewSet(ModelViewSet):
    queryset = VideoCard.objects.all()
    serializer_class = CentralProcessingUnitModelSerializer
