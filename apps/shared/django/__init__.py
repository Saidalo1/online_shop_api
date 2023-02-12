from shared.django.functions import delete_main_photo, delete_all_photos, upload_image_product_url, \
    has_difference_images, upload_other_images_product_url
from shared.django.models import TimeBaseModel
from shared.django.permissions import IsAdminUserOrReadOnly, IsOwnerOrIsAdminOrReadOnly
from shared.django.serializers import GetUserNameSerializer
from shared.django.views import CRUdViewSet
