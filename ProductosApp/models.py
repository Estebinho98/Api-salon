from django.db import models
from CategoriaApp.models import Category

# Create your models here.
class Products(models.Model):
    title =models.CharField(max_length=255)
    price =models.DecimalField(max_digits=6, decimal_places=2)
    inventory =models.SmallIntegerField()
    description =models.TextField()
    category =models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title