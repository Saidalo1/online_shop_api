from django.urls import path, include
from rest_framework import routers

from orders.views import TypeModelViewSet, CompanyModelViewSet, \
    RatingModelViewSet, CommentsModelViewSet, SalesModelViewSet, BasketModelViewSet, OrderModelViewSet, \
    PaymentsModelViewSet, CentralProcessingUnitModelViewSet, VideoCardModelViewSet
from orders.views.computer_spare_part_handbook import ImagesModelCreateAPIView

router_v1 = routers.SimpleRouter()
router_v1.register('cpu', CentralProcessingUnitModelViewSet)
# router_v1.register('images', ImagesModelViewSet)
router_v1.register('company', CompanyModelViewSet)
router_v1.register('types', TypeModelViewSet)
router_v1.register('rating', RatingModelViewSet)
router_v1.register('comments', CommentsModelViewSet)
router_v1.register('sales', SalesModelViewSet)
router_v1.register('video_card', VideoCardModelViewSet)
router_v1.register('basket', BasketModelViewSet)
router_v1.register('orders', OrderModelViewSet)
router_v1.register('payment', PaymentsModelViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('images/', ImagesModelCreateAPIView.as_view()),
]
