from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from orders.models import Type, Company, Images, Rating, Comments, Sales, Basket, Order, Payments
from orders.serializers import TypeModelSerializer, CompanyModelSerializer, ImagesCreateModelSerializer, \
    RatingModelSerializer, CommentsModelSerializer, SalesModelSerializer, BasketModelSerializer, OrderModelSerializer, \
    PaymentsModelSerializer, ImagesListModelSerializer


class TypeModelViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeModelSerializer


class CompanyModelViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer


class ImagesModelCreateAPIView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesCreateModelSerializer
    parser_classes = (MultiPartParser,)


class ImagesModelListAPIView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesListModelSerializer


class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer


class CommentsModelViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsModelSerializer


class SalesModelViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesModelSerializer


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketModelSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class PaymentsModelViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsModelSerializer
