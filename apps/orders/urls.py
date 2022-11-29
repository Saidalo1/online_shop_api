from django.urls import path, include
from orders.views import TypeModelViewSet, CompanyModelViewSet, ImagesModelViewSet, \
    RatingModelViewSet, CommentsModelViewSet, SalesModelViewSet, BasketModelViewSet, OrderModelViewSet, \
    PaymentTypeModelViewSet, PaymentsModelViewSet, CentralProcessingUnitModelViewSet, VideoCardModelViewSet
from rest_framework import routers

router_v1 = routers.SimpleRouter()
router_v1.register('cpu', CentralProcessingUnitModelViewSet)
router_v1.register('images', ImagesModelViewSet)
router_v1.register('company', CompanyModelViewSet)
router_v1.register('types', TypeModelViewSet)
router_v1.register('rating', RatingModelViewSet)
router_v1.register('comments', CommentsModelViewSet)
router_v1.register('sales', SalesModelViewSet)
router_v1.register('clients', VideoCardModelViewSet)
router_v1.register('basket', BasketModelViewSet)
router_v1.register('orders', OrderModelViewSet)
router_v1.register('payment-type', PaymentTypeModelViewSet)
router_v1.register('payment', PaymentsModelViewSet)

urlpatterns = [
    path('orders/', include(router_v1.urls))
]
