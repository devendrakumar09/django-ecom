
from django.urls import path,include
from product.views import ProductsViewSet,CategoryViewSet,DiscountViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# CATEGORIES URLS
router.register(r'category',CategoryViewSet)
# DISCOUNT URLS
router.register(r'discount',DiscountViewSet)
# PRODUCT URLS
router.register(r'products',ProductsViewSet)

urlpatterns = [
    path('', include(router.urls))
]