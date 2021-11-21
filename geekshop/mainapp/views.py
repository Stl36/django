from django.core.management.commands import loaddata
from django.shortcuts import render
from .models import ProductCategory, Product
# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    products = Product.objects.all()
    context = {
        'title': 'GeekShop - Каталог',
        'products': products,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
