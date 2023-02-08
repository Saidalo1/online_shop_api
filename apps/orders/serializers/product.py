from django.db.models import F
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from orders.models import Product


class ProductModelSerializer(ModelSerializer):
    views = IntegerField(read_only=True)

    def to_representation(self, instance):
        Product.objects.filter(id=instance.id).update(views=F('views') + 1)
        return super().to_representation(instance)

    class Meta:
        model = Product
        exclude = ('updated_at',)
