from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import ModelSerializer, ValidationError

from orders.models import Type, Company, Images, Rating, Comments, Sales, Basket, Order, Payments


class TypeModelSerializer(ModelSerializer):
    class Meta:
        model = Type
        exclude = ()


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        exclude = ()


class ImagesCreateModelSerializer(ModelSerializer):

    def get_validators(self):
        model_name = self.context['request'].parser_context['kwargs']['content_type__model']
        if ContentType.objects.filter(model=model_name).exists():
            model = apps.get_model('orders', model_name)
            if model.objects.filter(id=self.context['request'].data['object_id']).exists():
                return super().get_validators()
            raise ValidationError("Object not found", 404)
        raise ValidationError("Model name is not valid", 404)

    def create(self, validated_data):
        model_name = self.context['request'].parser_context['kwargs']['content_type__model']
        validated_data['content_type'] = ContentType.objects.get(model=model_name)
        model = apps.get_model('orders', model_name)
        validated_data['object_id'] = model.objects.get(id=validated_data['object_id']).id
        return super().create(validated_data)

    class Meta:
        model = Images
        exclude = ()


class RatingModelSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ()


class CommentsModelSerializer(ModelSerializer):
    class Meta:
        model = Comments
        exclude = ()


class SalesModelSerializer(ModelSerializer):
    class Meta:
        model = Sales
        exclude = ()


class BasketModelSerializer(ModelSerializer):
    class Meta:
        model = Basket
        exclude = ()


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ()


class PaymentsModelSerializer(ModelSerializer):
    class Meta:
        model = Payments
        exclude = ()
