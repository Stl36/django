from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                'title': 'GeekShop | Авторизация',
                'form': form,
                'alert': True,
            }

            return render(request, 'authapp/login.html', context)
            # print(form.errors)
    else:
        form = UserLoginForm()

    context = {
        'title': 'GeekShop | Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    context = {
        'title': 'GeekShop | Регистрация',
    }
    return render(request, 'authapp/register.html', context)
