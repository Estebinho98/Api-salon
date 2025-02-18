from django.db import models
from ServiciosApp.models import Servicies
# Create your models here.
class Bookings(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    servicie = models.ManyToManyField(Servicies)
    date = models.DateTimeField()

    def __str__(self):
        return {self.name}, {self.last_name}
