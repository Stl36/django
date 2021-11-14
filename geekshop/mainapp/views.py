from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
    }
    return render(request, 'mainapp/products.html', context)
