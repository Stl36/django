from django.contrib import admin

# Register your models here.
from authapp.models import User

# admin.site.register(User)
from baskets.admin import BasketAdmin
from baskets.models import Basket


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = Basket
    inlines = (BasketAdmin,)