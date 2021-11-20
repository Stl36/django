from django.core.management.commands import loaddata
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
        'products':[
            {'name':'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'mini_desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'img_url' : '/vendor/img/products/Adidas-hoodie.png'},

            {'name': 'Синяя куртка The North Face',
             'price': 23725,
             'mini_desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'img_url': '/vendor/img/products/Blue-jacket-The-North-Face.png'},

            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': 3390,
             'mini_desc': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'img_url': '/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},

            {'name': 'Черный рюкзак Nike Heritage',
             'price': 2340,
             'mini_desc': 'Плотная ткань. Легкий материал.',
             'img_url': '/vendor/img/products/Black-Nike-Heritage-backpack.png'},

            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590,
             'mini_desc': 'Гладкий кожаный верх. Натуральный материал.',
             'img_url': '/vendor/img/products/Black-Dr-Martens-shoes.png'},
        ]
    }
    return render(request, 'mainapp/products.html', context)
