from django.contrib.contenttypes.models import ContentType
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from orders.models import CentralProcessingUnit, VideoCard, Images
from orders.serializers import CentralProcessingUnitModelSerializer, VideoCardModelSerializer
from shared.django import delete_main_photo, delete_all_photos


class CentralProcessingUnitModelViewSet(ModelViewSet):
    queryset = CentralProcessingUnit.objects.all()
    serializer_class = CentralProcessingUnitModelSerializer
    parser_classes = (MultiPartParser,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = {'price': ['gte', 'lte']}
    search_fields = ('name',)

    def destroy(self, request, *args, **kwargs):
        delete_main_photo(CentralProcessingUnit, kwargs['pk'])
        content_type_id = ContentType.objects.get(model=CentralProcessingUnit._meta.model_name).id
        delete_all_photos(Images, kwargs['pk'], content_type_id)
        return super().destroy(request, *args, **kwargs)


class VideoCardModelViewSet(ModelViewSet):
    queryset = VideoCard.objects.all()
    serializer_class = VideoCardModelSerializer
    parser_classes = (MultiPartParser,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = {'price': ['gte', 'lte']}
    search_fields = ('name',)

    def destroy(self, request, *args, **kwargs):
        delete_main_photo(VideoCard, kwargs['pk'])
        content_type_id = ContentType.objects.get(model=VideoCard._meta.model_name).id
        delete_all_photos(Images, kwargs['pk'], content_type_id)
        return super().destroy(request, *args, **kwargs)
