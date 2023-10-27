from django.db import models


# CATEGORY MODEL
class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

# DISCOUNT MODEL
class DiscountModel(models.Model):
    id = models.AutoField(primary_key=True)
    discount = models.IntegerField()
    create_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

# PRODUCT MODEL.
class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    addby = models.IntegerField(null=True)
    category_id = models.IntegerField(null=True)
    discount_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()        
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='static/products')
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
