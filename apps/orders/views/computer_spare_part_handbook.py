from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from orders.models import Type, Company, Images, Rating, Comments, Sales, Basket, Order, PaymentType, Payments
from orders.serializers import TypeModelSerializer, CompanyModelSerializer, ImagesModelSerializer, \
    RatingModelSerializer, CommentsModelSerializer, SalesModelSerializer, BasketModelSerializer, OrderModelSerializer, \
    PaymentTypeModelSerializer, PaymentsModelSerializer


class TypeModelViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeModelSerializer


class CompanyModelViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer


# class ImagesModelViewSet(ModelViewSet):
#     queryset = Images.objects.all()
#     serializer_class = ImagesModelSerializer
#     parser_classes = (MultiPartParser,)
#
#     def destroy(self, request, *args, **kwargs):
#         if Images.objects.get(id=kwargs.get('pk')):
#             image_url = Images.objects.get(id=kwargs.get('pk')).image.url
#             os.remove(BASE_DIR + image_url)
#         return super().destroy(request, *args, **kwargs)


class ImagesModelCreateAPIView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesModelSerializer
    parser_classes = (MultiPartParser,)


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


class PaymentTypeModelViewSet(ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeModelSerializer


class PaymentsModelViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsModelSerializer
