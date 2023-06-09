from django.db import models

# Create your models here.
class car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField()
