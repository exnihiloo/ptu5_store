from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'slug',
                    'price', 'in_stock', 'created',
                    'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
