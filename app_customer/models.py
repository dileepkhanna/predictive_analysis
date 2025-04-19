from django.db import models


# Create your models here.
class CustomerModelRegister(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.PositiveBigIntegerField()
    date_of_birth = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class CustomerInitiationForm(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    contact = models.PositiveBigIntegerField()
    building_type = models.CharField(max_length=200)
    land_area = models.CharField(max_length=200)
    soil_type = models.CharField(max_length=200)
    soil_condition = models.CharField(max_length=200)
    foundation = models.CharField(max_length=200)
    water = models.CharField(max_length=200)
    cost = models.CharField(max_length=200, null=True)
    send_customer = models.BooleanField(default=False)
    request_estimation = models.BooleanField(default=False)
    price_send = models.BooleanField(default=False)
    accept_work = models.BooleanField(default=False)
