from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)

    @staticmethod
    def get_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
