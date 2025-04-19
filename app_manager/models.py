from django.db import models


# Create your models here.
class ManagerModelRegister(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.PositiveBigIntegerField()
    date_of_birth = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class MaterialDetails(models.Model):
    cement = models.IntegerField(null=True)
    sand = models.IntegerField(null=True)
    aggregate = models.IntegerField(null=True)
    steel = models.IntegerField(null=True)
    paint = models.IntegerField(null=True)
    bricks = models.IntegerField(null=True)
    tiles = models.IntegerField(null=True)
    land = models.IntegerField(null=True)
    supply_id = models.CharField(max_length=200, null=True)
    confirm = models.BooleanField(default=False)
    send_from_vendor = models.BooleanField(default=False)
    send_to_analyse = models.BooleanField(default=False)
