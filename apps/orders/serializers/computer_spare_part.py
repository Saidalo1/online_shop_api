from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from orders.models import CentralProcessingUnit, VideoCard


class CentralProcessingUnitModelSerializer(ModelSerializer):
    views = IntegerField(default=0, read_only=True)

    def to_representation(self, instance):
        instance.views += 1
        CentralProcessingUnit.objects.filter(id=instance.id).update(views=instance.views)
        return super().to_representation(instance)

    class Meta:
        model = CentralProcessingUnit
        exclude = ('updated_at', 'slug')


class VideoCardModelSerializer(ModelSerializer):
    class Meta:
        model = VideoCard
        exclude = ()
