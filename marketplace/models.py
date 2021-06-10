from django.db import models
from seller.models import Seller

# Create your models here.
class Marketplace(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    sellers = models.ManyToManyField(Seller)

    def __str__(self):
        return self.name
