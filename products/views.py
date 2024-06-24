from django.shortcuts import render
from . models import Product, ContactUs
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request, 'index.html')


def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list = Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,12)
    product_list=product_paginator.get_page(page)
    context = {'products':product_list}
    return render(request, 'products.html', context)


def detail_product(request,pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_details.html', context)


def contact_us(request):
    return render(request, 'contact_page.html')


def read_blogs(request):
    return render (request, 'read_blogs.html')


def blog_post(request):
    return render (request, 'blog_post.html')