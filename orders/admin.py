from django.contrib import admin
from . models import Order, OrderedItem

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderedItem)