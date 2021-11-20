
from django.urls import path


from mainapp.views import index,products

urlpatterns = [
    path('', products, name='products'),
]

