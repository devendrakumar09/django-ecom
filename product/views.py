
from rest_framework import viewsets
from product.models import ProductModel
from product.serializers import ProductSerializers

# Create your views here.
#PRODUCT VIEWAS.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers