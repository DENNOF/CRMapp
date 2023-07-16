from django.db import models


class employee(models.Model):
    Fname = models.CharField(max_length=20, default="hd")
    Lname = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)
    age = models.CharField(max_length=20, default='hes')

# Create your models here.
