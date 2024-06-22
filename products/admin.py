from django.contrib import admin
from . models import Product, ReadBlogs, ContactUs, BannerContent

# Register your models here.
admin.site.register(Product)
admin.site.register(ReadBlogs)
admin.site.register(ContactUs)
admin.site.register(BannerContent)