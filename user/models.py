from django.db import models

class reg(models.Model):
   name = models.CharField(max_length=100,null=True, blank=True)
   des=models.TextField()
   image = models.ImageField(upload_to="pict/")
