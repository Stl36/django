from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryEditForm
from authapp.models import User
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_users'))

#############################################################################################

@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products-read.html', context)




@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-categories-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, pk):
    user_select = ProductCategory.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductCategoryEditForm(instance=user_select, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = ProductCategoryEditForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'user_select': user_select
    }

    return render(request, 'admins/admin-categories-update-delete.html', context)