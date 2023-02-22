from django.urls import path, include
from rest_framework import routers

from orders.views import CompanyReadOnlyModelViewSet, RatingModelViewSet, BasketModelViewSet, \
    OrderReadOnlyViewSet, ProductReadOnlyModelViewSet, ImagesModelListAPIView, ImagesModelDetailAPIView, \
    CommentsListAPIView
from orders.views.product_handbook import CommentsRetrieveUpdateDestroyAPIView, CommentsCreateAPIView, \
    CategoryReadOnlyModelViewSet, SubCategoryReadOnlyModelViewSet

router_v1 = routers.SimpleRouter()
router_v1.register('products', ProductReadOnlyModelViewSet, 'product')
router_v1.register('company', CompanyReadOnlyModelViewSet, 'company')
router_v1.register('rating', RatingModelViewSet, 'rating')
router_v1.register('basket', BasketModelViewSet, 'basket')
router_v1.register('orders/get-my-orders', OrderReadOnlyViewSet, 'order')
router_v1.register('category', CategoryReadOnlyModelViewSet, 'category')
router_v1.register('sub_category', SubCategoryReadOnlyModelViewSet, 'sub_category')

urlpatterns = [
    path('', include(router_v1.urls)),

    # product-images
    path('products/<int:product_pk>/images/', ImagesModelListAPIView.as_view(), name='images-list'),
    path('products/<int:product_pk>/images/<int:pk>/', ImagesModelDetailAPIView.as_view(), name='images-detail'),

    # product-comments
    path('products/<int:product_pk>/comments/', CommentsListAPIView.as_view(), name='comments-list'),
    path('products/<int:product_pk>/comments/create/', CommentsCreateAPIView.as_view(), name='comments-create'),
    path('products/<int:product_pk>/comments/<int:pk>/', CommentsRetrieveUpdateDestroyAPIView.as_view(),
         name='comments-detail'),
]
