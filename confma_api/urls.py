from django.urls import include, path
from rest_framework import routers
from confma_api import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet, basename="client")
router.register(r'cloth', views.ClothViewSet)
router.register(r'cotizacion', views.CotizacionViewSet)
router.register(r'rental', views.RentalViewSet)

#
app_name = "confma_api"
urlpatterns = [
    path('', include(router.urls)),
]

