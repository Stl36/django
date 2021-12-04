from django.urls import path

from mainapp.views import index, products

app_name = 'mainapp'
urlpatterns = [
    path('', products, name='products'),
]
