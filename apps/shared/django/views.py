from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet


class SampleViewSet(CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    GenericViewSet):
    pass
