from orders.models import Type, Company, Images, Rating, Comments, Sales, Basket, Order, PaymentType, Payments
from rest_framework.serializers import ModelSerializer


class TypeModelSerializer(ModelSerializer):
    class Meta:
        model = Type
        exclude = ()


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        exclude = ()


class ImagesModelSerializer(ModelSerializer):
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


class PaymentTypeModelSerializer(ModelSerializer):
    class Meta:
        model = PaymentType
        exclude = ()


class PaymentsModelSerializer(ModelSerializer):
    class Meta:
        model = Payments
        exclude = ()
