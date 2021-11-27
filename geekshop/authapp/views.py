from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfilerForm


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
            messages.success(request,'Вы успешно зарегестрировались')
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


def profile(request):

    context = {
        'title': 'Geeshop | Профиль',
        'form' : UserProfilerForm(),
    }
    return render(request, 'authapp/profile.html', context)

def logout(request):
    auth.logout(request)
    return render(request, 'mainapp\index.html')
