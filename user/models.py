from django.db import models

class reg(models.Model):
    username = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    pwd = models.CharField(max_length=100,null=True, blank=True)
    image = models.ImageField(upload_to="pict/")
