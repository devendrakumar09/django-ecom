from rest_framework import serializers
from product.models import ProductModel

#  // PRODUCT serializers
class ProductSerializers(serializers.HyperlinkedModelSerializer):
    product_id = serializers.ReadOnlyField()
    class Meta:
        model = ProductModel
        fields = "__all__"