from django.db import models


# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Address(models.Model):
    number = models.CharField(max_length=5)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.street} - {self.district} - {self.number}"