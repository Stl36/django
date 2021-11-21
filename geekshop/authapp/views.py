from django.shortcuts import render

# Create your views here.


def login(request):
    context = {
        'title': 'GeekShop | Авторизация',
    }
    return render(request, 'authapp/index.html', context)

def register(request):
    context = {
        'title': 'GeekShop | Регистрация',
    }
    return render(request, 'authapp/register.html', context)