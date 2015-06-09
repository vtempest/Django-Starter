from django.db import models

from django.contrib.auth.models import User

class TableEntry(models.Model):
    title = models.CharField(max_length=50)

class FoodEntry(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

class ReservationEntry(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    table = models.ForeignKey(TableEntry)
    foodList = models.ManyToManyField(FoodEntry)
