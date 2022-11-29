from orders.models import CentralProcessingUnit, VideoCard
from rest_framework.serializers import ModelSerializer


class CentralProcessingUnitModelSerializer(ModelSerializer):
    class Meta:
        model = CentralProcessingUnit
        exclude = ()


class VideoCardModelSerializer(ModelSerializer):
    class Meta:
        model = VideoCard
        exclude = ()
