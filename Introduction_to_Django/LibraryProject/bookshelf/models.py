from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

# class Product(models.Model):
#     product_name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.CharField(max_length=300)