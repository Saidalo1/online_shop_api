from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from orders.models import Type, Company, Images, Rating, Comments, Sales, Basket, Order, Payments
from orders.serializers import TypeModelSerializer, CompanyModelSerializer, RatingModelSerializer, \
    CommentsModelSerializer, SalesModelSerializer, BasketModelSerializer, OrderModelSerializer, \
    PaymentsModelSerializer, ImagesListModelSerializer, CommentsListModelSerializer, ImagesCreateUpdateModelSerializer
from shared.django import IsOwnerOrIsAdminOrReadOnly, SampleViewSet


class TypeModelViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeModelSerializer


class CompanyModelViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer


class ImagesModelCreateAPIView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesCreateUpdateModelSerializer
    parser_classes = (MultiPartParser,)


class ImagesModelUpdateAPIView(UpdateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesCreateUpdateModelSerializer
    parser_classes = (MultiPartParser,)


class ImagesModelListAPIView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesListModelSerializer


class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer


class CommentsModelViewSet(SampleViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsModelSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)


class CommentsListAPIView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsListModelSerializer

    def get(self, request, *args, **kwargs):
        if ContentType.objects.filter(model=kwargs['model_name']).exists():
            model = ContentType.objects.get(model=f"{kwargs['model_name']}").model_class()
            model_id = ContentType.objects.filter(model=kwargs['model_name']).first().id
            if model.objects.filter(id=kwargs['object_id']).exists():
                object_id = model.objects.first(id=kwargs['object_id']).id
                return Comments.objects.filter(content_type=model_id, object_id=object_id)
            raise ValidationError("Object not found", 404)
        raise ValidationError("Page not found", 404)


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
