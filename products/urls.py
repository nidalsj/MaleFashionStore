from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products_list', views.list_products, name='list_product'),
    path('product_details/<pk>', views.detail_product, name='product_details'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('read_blogs', views.read_blogs, name='read_blogs'),
    path('blog_post/<pk>', views.blog_post, name='blog_post'),

]
