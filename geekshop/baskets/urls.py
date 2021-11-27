from django.urls import path
# from authapp.views import
from authapp.views import login, register, logout, profile
from baskets.views import basket_add, basket_remove

app_name = 'baskets'
urlpatterns = [

      path('add/<int:id>', basket_add, name='basket_add'),
      path('remove/<int:basket_id>', basket_remove, name='basket_remove'),

]
