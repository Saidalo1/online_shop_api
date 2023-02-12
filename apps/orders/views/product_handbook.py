from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from orders.models import Company, ProductRating, ProductComment, Basket, Order, Payment, ProductImage
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
        return ProductImage.objects.filter(product_id=self.kwargs.get('product_pk'))


class ImagesModelDetailAPIView(RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ImagesModelSerializer


class RatingModelViewSet(ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = RatingModelSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def get_queryset(self):
        return ProductRating.objects.filter(user_id=self.request.user.pk)


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
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return ProductComment.objects.filter(product_id=self.kwargs.get('product_pk'))


class CommentsCreateAPIView(CreateAPIView):
    serializer_class = CommentsModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['product_pk'] = self.kwargs.get('product_pk')
        return context

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CommentsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsModelSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def get_queryset(self):
        return ProductComment.objects.filter(product_id=self.kwargs.get('product_pk'))
