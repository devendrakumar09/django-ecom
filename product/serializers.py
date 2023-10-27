from rest_framework import serializers
from product.models import ProductModel,CategoryModel,DiscountModel


# CATEGORY serializers
class CategorySerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = CategoryModel
        fields = "__all__"
    
# DISCOUNT serializers
class DiscountSerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = DiscountModel
        fields = "__all__"
    

#  // PRODUCT serializers
class ProductSerializers(serializers.HyperlinkedModelSerializer):
    product_id = serializers.ReadOnlyField()
    class Meta:
        model = ProductModel
        fields = "__all__"