from django.urls import path, include
from rest_framework import routers

from orders.views import CompanyReadOnlyModelViewSet, RatingModelViewSet, BasketModelViewSet, \
    OrderReadOnlyViewSet, ProductReadOnlyModelViewSet, ImagesModelListAPIView, ImagesModelDetailAPIView, \
    CommentsListAPIView
from orders.views.product_handbook import CommentsRetrieveUpdateDestroyAPIView, CommentsCreateAPIView

router_v1 = routers.SimpleRouter()
router_v1.register('products', ProductReadOnlyModelViewSet, 'products')
router_v1.register('company', CompanyReadOnlyModelViewSet, 'company')
router_v1.register('rating', RatingModelViewSet, 'rating')
router_v1.register('basket', BasketModelViewSet, 'basket')
router_v1.register('orders/get-my-orders', OrderReadOnlyViewSet, 'orders')

urlpatterns = [
    path('', include(router_v1.urls)),

    # product-images
    path('products/<int:product_pk>/images/', ImagesModelListAPIView.as_view(), name='images_list'),
    path('products/<int:product_pk>/images/<int:pk>/', ImagesModelDetailAPIView.as_view(), name='images_detail'),

    # product-comments
    path('products/<int:product_pk>/comments/', CommentsListAPIView.as_view(), name='comments_list'),
    path('products/<int:product_pk>/comments/create/', CommentsCreateAPIView.as_view(), name='comments_create'),
    path('products/<int:product_pk>/comments/<int:pk>/', CommentsRetrieveUpdateDestroyAPIView.as_view()),
]
