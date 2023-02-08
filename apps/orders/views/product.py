from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ReadOnlyModelViewSet

from orders.models import Product
from orders.serializers import ProductModelSerializer


class ProductReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    parser_classes = (MultiPartParser,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = {'price': ['gte', 'lte']}
    search_fields = ('name',)
