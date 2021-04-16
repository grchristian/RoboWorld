from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=200)
    
class Reto(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()
