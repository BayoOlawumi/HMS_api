from django.db import models

# Create your models here.

""" Return category
    This model handles the category of product, with many to one relationship
"""


class Category(models.Model):
    name = models.CharField(blank=False, max_length=40)
    unique_color = models.CharField(blank=True, max_length=15)

    def __str__(self):
        return self.name


""" Return a Product Model
    This class provides structure for the product database
"""


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=40)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    no_available = models.DecimalField(max_digits=10, decimal_places=0, blank=False)
    no_of_intake = models.DecimalField(max_digits=10, decimal_places=0, blank=False)

    def __str__(self):
        return self.name
