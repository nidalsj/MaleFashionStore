from django.shortcuts import render
from . models import Product, ContactUs, BannerContent, ReadBlogs
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    banner_content = BannerContent.objects.first()
    featured_products = Product.objects.order_by('priority')[:8]
    context = {'banner_content': banner_content,
               'featured_products': featured_products}

    return render(request, 'index.html', context)


def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list = Product.objects.order_by('priority')
    product_count = Product.objects.count()
    product_paginator=Paginator(product_list,12)
    product_list=product_paginator.get_page(page)
    context = {'products':product_list,
               'product_count':product_count}
    return render(request, 'products.html', context)


def detail_product(request,pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_details.html', context)


def contact_us(request):
    form_submitted = False
    if request.method == "POST":
        name = request.POST.get('fullname')
        usermail = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ctquery = ContactUs(full_name=name, email_address=usermail, subject=subject, message=message)
        ctquery.save() 
        
        form_submitted = True
        messages.success(request, 'Your message has been submitted successfully!')
    return render(request, 'contact_page.html', {'form_submitted': form_submitted})


def read_blogs(request):
    blogs_list = ReadBlogs.objects.all()[:9]
    context = {'blogs_list': blogs_list}
    return render (request, 'read_blogs.html', context)


def blog_post(request, pk):
    blog_post = ReadBlogs.objects.get(pk=pk)
    context = {'blog_post': blog_post}
    return render (request, 'blog_post.html', context)