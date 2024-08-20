from django.db import models
from decimal import Decimal


# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        return iter(self.dishes.filter(is_visible=True))


    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['sort']

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='dish_photos')
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    sort = models.PositiveSmallIntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ['sort']

    def __str__(self):
        return self.name
