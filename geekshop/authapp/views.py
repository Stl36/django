from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfilerForm
from baskets.models import Basket


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
            messages.success(request, 'Вы успешно зарегестрировались')
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


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfilerForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():  # даже с некорректными данными проверка успешна. Почему?
            messages.success(request, 'Профиль обновлен')
            form.save()
        else:
            messages.error(request, form.errors)

    context = {
        'title': 'Geeshop | Профиль',
        'form': UserProfilerForm(instance=request.user),
        'baskets': Basket.objects.filter(user=request.user),

    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp\index.html')
