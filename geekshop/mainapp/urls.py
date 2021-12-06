from django.urls import path

from mainapp.views import index, products, ProductDetail

app_name = 'mainapp'
urlpatterns = [
    path('', products, name='products'),
    path('catefory/<int:id_category>', products, name='category'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='detail'),

]
