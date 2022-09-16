from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from .models import *
from rest_framework import filters
from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


class ComputerSparePartsViewSet(viewsets.ModelViewSet):
    queryset = ComputerSparePart.objects.all()
    serializer_class = CSPSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'description']
    filterset_fields = ['name', 'description']
    ordering_fields = ['name', 'description']

    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            if request.POST.get("type") != "2":
                if request.POST.get("processor_series") == '' and request.POST.get("graphics_processing_unit") == '' and request.POST.get("graphics_processing_unit_frequency") == '' and request.POST.get("video_memory_type") == '':
                    return super().create(request, *args, **kwargs)
                else:
                    pass

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

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, template_name='login.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect(reverse_lazy('index'))
        return render(request, template_name='login.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})

def logout_request(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse_lazy("index"))

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        form = RegisterForm(data=request.POST)
        if form.is_valid():

            user = form.instance
            user.set_password(request.POST['password'])
            form.save()

            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
                return redirect(reverse_lazy('index'))
            return render(request, template_name='register.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})
        
        return render(request, template_name='register.html', context={'form': form})
