from pyexpat import model
from django.db import models

# Create your models here.

class familia (models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    coreo=models.CharField(max_length=200)

