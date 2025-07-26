
from django.db import models


# Create your models here.
class VendorModelRegister(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.PositiveBigIntegerField()
    date_of_birth = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
