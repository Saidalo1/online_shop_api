from django.db.models import F
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from orders.models import CentralProcessingUnit, VideoCard


class CentralProcessingUnitModelSerializer(ModelSerializer):
    views = IntegerField(read_only=True)

    def to_representation(self, instance):
        CentralProcessingUnit.objects.filter(id=instance.id).update(views=F('views') + 1)
        return super().to_representation(instance)

    class Meta:
        model = CentralProcessingUnit
        exclude = ('updated_at', 'slug')


class VideoCardModelSerializer(ModelSerializer):
    class Meta:
        model = VideoCard
        exclude = ()
