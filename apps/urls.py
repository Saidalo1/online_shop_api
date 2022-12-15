from django.conf.urls.static import static
from django.urls import include, path

from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
      path('', include('orders.urls')),
      # path('account/', include('users.urls')),
  ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
