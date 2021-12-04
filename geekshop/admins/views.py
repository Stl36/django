from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from authapp.models import User


def index(request):
    return render(request, 'admins/admin.html')


def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update(request, pk):
    user_select = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = UserAdminProfileForm(instance=user_select, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'user_select': user_select
    }

    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_delete(request):
    return render(request, 'admins/admin-users-update-delete.html')
