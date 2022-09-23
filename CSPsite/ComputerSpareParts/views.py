from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from .models import *
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
<<<<<<< HEAD

=======
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
>>>>>>> e03e7b32b56f88bb5ab26a09cd309b68b28add5b

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ComputerSparePartsViewSet(viewsets.ModelViewSet):
    queryset = ComputerSparePart.objects.all()
    serializer_class = CSPSerializer
    pagination_class = PageNumberPagination
<<<<<<< HEAD
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'description']
    filterset_fields = '__all__'
    ordering_felds = '__all__'
=======
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'
>>>>>>> e03e7b32b56f88bb5ab26a09cd309b68b28add5b
    permission_classes = [IsAdminUser|ReadOnly]

    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            if request.POST.get("type") != "2":
                if request.POST.get("processor_series") != '':
                    return Response({'processor_series не должен быть пустым'}, status=406)
                elif request.POST.get("graphics_processing_unit") != '': 
                    return Response({'graphics_processing_unit не должен быть пустым \n'}, status=406)
                elif request.POST.get("graphics_processing_unit_frequency") != '':
                    return Response({'graphics_processing_unit_frequency не должен быть пустым \n'}, status=406)
                elif request.POST.get("video_memory_type") != '':
                    return Response({'video_memory_type не должен быть пустым \n'}, status=406)
                else:
                    return super().create(request, *args, **kwargs)

class CSPImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = CSPImagesSerializer
    pagination_class = PageNumberPagination


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = PageNumberPagination


class TypesViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    pagination_class = PageNumberPagination


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = PageNumberPagination


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    pagination_class = PageNumberPagination


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    pagination_class = PageNumberPagination


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    pagination_class = PageNumberPagination

    def basket(request):
        basket = Basket()
        basket.computer_spare_part = request.data
        basket.user = request.user
        basket.save()


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    pagination_class = PageNumberPagination


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            return super().create(request, *args, **kwargs)


