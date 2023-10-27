
from django.urls import path,include
from product.views import ProductsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products',ProductsViewSet)

urlpatterns = [
    path('', include(router.urls))
]