from shared.django.functions import delete_main_photo, delete_all_photos, upload_name_cpu, upload_name_video_card
from shared.django.models import CSPBaseModel, SlugBaseModel, TimeBaseModel
from shared.django.permissions import IsAdminUserOrReadOnly, IsOwnerOrIsAdminOrReadOnly
from shared.django.serializers import GetUserNameSerializer
from shared.django.views import SampleViewSet
