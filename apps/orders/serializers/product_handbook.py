from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from orders.models import Company, ProductImage, ProductRating, ProductComment, Basket, Order, Payment
from shared.django import GetUserNameSerializer


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        exclude = ()


class ImagesModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ()


class RatingModelSerializer(ModelSerializer):
    class Meta:
        model = ProductRating
        exclude = ()


class CommentsModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['user'] = GetUserNameSerializer(instance.user).data
        return represent

    def create(self, validated_data):
        return super().create(validated_data)

    def save(self, **kwargs):
        kwargs['product_id'] = self.context['product_pk']
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
        model = ProductComment
        exclude = ('is_active', 'product',)


class CommentsListModelSerializer(ModelSerializer):
    class Meta:
        model = ProductComment
        exclude = ()


class BasketModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

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
