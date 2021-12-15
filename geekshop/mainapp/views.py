from django.core.management.commands import loaddata
from django.shortcuts import render
from .models import ProductCategory, Product
import os
from django.views.generic import DetailView

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    products = Product.objects.all()
    context = {
        'title': 'GeekShop | Каталог',
        'products': products,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода инфо о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
