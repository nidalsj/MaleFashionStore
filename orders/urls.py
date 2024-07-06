from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.show_cart, name='cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<pk>',views.remove_item_from_cart,name='remove_item'),


]
