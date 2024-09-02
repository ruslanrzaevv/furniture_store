from django.contrib import admin
from goods.models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','slug']
    list_display_links = ['name', 'slug']

    

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quanity', 'price', 'dicount',]
    list_display_link = ['name', 'id']
    list_editable = ['dicount']
    search_fields = ['name', 'description']
    list_filter = ['dicount', 'quanity', 'category']
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'dicount'),
        'quanity',
    ]

