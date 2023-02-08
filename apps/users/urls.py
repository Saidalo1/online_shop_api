from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import UserCreateApiView, GetMeApiView, CustomTokenObtainPairView, ForgotPasswordApiView, \
    ChangePasswordApiView, ActivateUserApiView

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('forgot-password/', ForgotPasswordApiView.as_view(), name='forget_password'),
    path('change-password/', ChangePasswordApiView.as_view(), name='change_password'),
    path('activate_account/<str:uidb64>/<str:token>', ActivateUserApiView.as_view(), name='activate_user'),
    path('get-me/', GetMeApiView.as_view(), name='get_me'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
