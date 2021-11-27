from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:products'))
            # else:
            #     # print(form.errors)
            #     form = UserLoginForm()
            #     context = {
            #         'title': 'GeekShop | Авторизация',
            #         'form': form,
            #         'alert': True,
            #     }
            #
            # return render(request, 'authapp/login.html', context)

    else:
        form = UserLoginForm()

    context = {
        'title': 'GeekShop | Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
        # else:
        #     # print(form.errors)
        #     form = UserRegisterForm()
        #     context = {
        #         'title': 'GeekShop | Регистрация',
        #         'form': form,
        #         'alert': True,
        #     }
        #
        #     return render(request, 'authapp/register.html', context)

    else:
        form = UserRegisterForm()

    context = {
        'title': 'GeekShop | Регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp\index.html')
