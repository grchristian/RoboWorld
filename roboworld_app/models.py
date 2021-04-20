from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    Userid = models.AutoField(primary_key=False)
    nombre = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    
class Reto(models.Model):
    Userid = models.ForeignKey(User, on_delete=models.CASCADE)
    minutos_jugados = models.IntegerField()
    minimo = models.IntegerField()


class Level(models.Model):
    Nivelid = models.models.AutoField(primary_key=True)
    level_number = models.IntegerField()
    enemigo = models.CharField(max_length=30)
    dificultad = models.IntegerField()
    duracion_indivudual = models.IntegerField()
  


class Engranes(models.Model):
    sessionObtained = models.IntegerField()
    number = models.IntegerField()


class Sesion(models.Model):
    SessionId = models.IntegerField()
    UserID = models.IntegerField()
    started = models.IntegerField()
    ended = models.IntegerField()
    score = models.IntegerField()



class Recompensas(models.Model):
    recompensasid = models.IntegerField()
    engranes_necesarios = models.IntegerField()
    top_score_global = models.IntegerField()
    top_five = models.IntegerField()


class Prueba(models.Model):
    Levelid = models.IntegerField()
    SesionID = models.IntegerField()
    success = models.BooleanField() 

    
