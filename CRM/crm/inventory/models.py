from django.db import models

class inventory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000) 
    quantity = models.IntegerField()
# Create your models here.

