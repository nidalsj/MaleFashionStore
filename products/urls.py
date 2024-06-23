from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products_list', views.list_products, name='list_product'),
    path('product_details/<pk>', views.detail_product, name='product_details'),
]
