
from django.urls import path,include
from product.views import ProductsViewSet,CategoryViewSet,DiscountViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category',CategoryViewSet)
router.register(r'discount',DiscountViewSet)
router.register(r'products',ProductsViewSet)
urlpatterns = [
    path('', include(router.urls))
]