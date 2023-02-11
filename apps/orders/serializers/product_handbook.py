from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from orders.models import Company, ProductImages, ProductRating, ProductComments, Basket, Order, Payment
from shared.django import GetUserNameSerializer


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        exclude = ()


class ImagesModelSerializer(ModelSerializer):

    class Meta:
        model = ProductImages
        exclude = ()


class RatingModelSerializer(ModelSerializer):
    class Meta:
        model = ProductRating
        exclude = ()


class CommentsModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    product = HiddenField(default=int)

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['user'] = GetUserNameSerializer(instance.user).data
        return represent

    def create(self, validated_data):
        return super().create(validated_data)

    def save(self, **kwargs):
        return super().save(**kwargs)

    @staticmethod
    def get_reply_count(obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    @staticmethod
    def get_author(obj):
        return obj.author.username

    class Meta:
        model = ProductComments
        exclude = ('is_active',)


class CommentsListModelSerializer(ModelSerializer):
    class Meta:
        model = ProductComments
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
        model = Payment
        exclude = ()
