from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def list_products(request):
    return render(request, 'products.html')


def detail_product(request):
    return render(request, 'product_details.html')