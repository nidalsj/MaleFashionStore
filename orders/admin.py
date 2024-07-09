from django.contrib import admin
from . models import Order, OrderedItem, Coupon

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(Coupon)