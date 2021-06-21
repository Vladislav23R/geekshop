from django.contrib import admin

from .models import ProductCategory, Product

# Register your models here.
admin.site.register(ProductCategory)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    ordering = ('-price',)
    search_fields = ('name',)
