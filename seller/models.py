from django.db import models


# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)

    def __str__(self):
        return self.name
