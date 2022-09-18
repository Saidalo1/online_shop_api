from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_view, name='register'),
]