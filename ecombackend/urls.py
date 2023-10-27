
# from django.contrib import admin
from django.urls import path,include
from .views import index

urlpatterns = [
    # path('admin/', admin.site.urls),

    path("",index),

    # All APIS URLS fromm Product App
    path('api/v1/', include('product.urls'))
]
