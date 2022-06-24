from django.contrib import admin

from .models import category
from .models import customer
from .models import product

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(product.Product)
admin.site.register(category.Category)
admin.site.register(customer.Customer)
