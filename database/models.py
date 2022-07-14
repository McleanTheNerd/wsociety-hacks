from django.db import models

# Create your models here.
class Device_info(models.Model):
    id = models.AutoField(primary_key=True)
    Cc = models.CharField(max_length=10000)
    ram = models.CharField(max_length=10000)
    Ptf = models.CharField(max_length=10000)
    Brw = models.CharField(max_length=100000)
    Ven = models.CharField(max_length=100000)
    Ht = models.CharField(max_length=100000)
    Wd = models.CharField(max_length=100000)
    Os = models.CharField(max_length=10000)


class Device_location(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=10000)
    longitude = models.CharField(max_length=10000)
    accuracy = models.CharField(max_length=10000)
    altitude = models.CharField(max_length=100000)
    dir = models.CharField(max_length=100000)
    speed = models.CharField(max_length=100000)
