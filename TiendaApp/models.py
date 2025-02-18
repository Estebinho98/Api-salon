from django.db import models
from ProductosApp.models import Products
# Create your models here.

class Buy(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    products = models.ManyToManyField(Products)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return {self.name}, {self.last_name}