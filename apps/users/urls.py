from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import UserCreateApiView, GetMeApiView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('get-me/', GetMeApiView.as_view(), name='get_me'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
