from django.db import models

# Create your models here.


class Place(models.Model):
    addr = models.CharField(max_length=100)


class CountryData(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()
