
from rest_framework import viewsets
from product.models import ProductModel,CategoryModel,DiscountModel
from product.serializers import ProductSerializers,CategorySerializers,DiscountSerializers

# CATEGORY VIEW SET
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers

# DISCOUNT VIEW SET
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountSerializers

# PRODUCT VIEWAS SET.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers