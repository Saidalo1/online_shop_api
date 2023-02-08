from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from orders.models import Company, Rating, ProductComments, Basket, Order, Payment, ProductImages
from orders.serializers import CompanyModelSerializer, RatingModelSerializer, \
    CommentsModelSerializer, BasketModelSerializer, OrderModelSerializer, \
    PaymentsModelSerializer, ImagesModelSerializer
from shared.django import IsOwnerOrIsAdminOrReadOnly


class CompanyReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer


class ImagesModelListAPIView(ListAPIView):
    serializer_class = ImagesModelSerializer

    def get_queryset(self):
        return ProductImages.objects.filter(product_id=self.kwargs.get('product_pk'))


class ImagesModelDetailAPIView(RetrieveAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ImagesModelSerializer


class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def get_queryset(self):
        return Rating.objects.filter(user_id=self.request.user.pk)


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketModelSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def get_queryset(self):
        return Basket.objects.filter(user_id=self.request.user.pk)


class OrderReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.pk)


class PaymentsModelViewSet(ModelViewSet):
    serializer_class = PaymentsModelSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def get_queryset(self):
        return Payment.objects.filter(user_id=self.request.user.pk)


class CommentsListAPIView(ListAPIView):
    serializer_class = CommentsModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ProductComments.objects.filter(user_id=self.request.user.pk)


class CommentsCreateAPIView(CreateAPIView):
    serializer_class = CommentsModelSerializer
    permission_classes = (IsAuthenticated,)


class CommentsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsModelSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def get_queryset(self):
        return ProductComments.objects.filter(product_id=self.kwargs.get('product_pk'))
