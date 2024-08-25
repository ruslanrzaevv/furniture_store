from django.contrib import admin
from carts.models import Cart

@admin.register(Cart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
