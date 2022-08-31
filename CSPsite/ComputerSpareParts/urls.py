from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'ComputerSparePart', ComputerSparePartsViewSet)
router.register(r'CSPImages', CSPImagesViewSet)
router.register(r'Company', CompanyViewSet)
router.register(r'Types', TypesViewSet)
router.register(r'Rating', RatingViewSet)
router.register(r'Comments', CommentsViewSet)
router.register(r'Sales', SalesViewSet)
router.register(r'Clients', ClientsViewSet)
router.register(r'Basket', BasketViewSet)
router.register(r'Orders', OrdersViewSet)
router.register(r'Payments', PaymentsViewSet)
router.register(r'Party', PartyViewSet)

urlpatterns = [

] + router.urls
