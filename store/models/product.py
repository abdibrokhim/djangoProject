from django.db import models
from .category import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=254, default='', blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/products/')

    @staticmethod
    def get_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id_in=ids)

    @staticmethod
    def get_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_products()

    def __str__(self):
        return self.name
