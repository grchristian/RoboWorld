from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=200)
    
class Reto(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()


class Level(models.Model):
    Levelid = models.IntegerField()
    level_number = models.IntegerField()
    enemigo = models.CharField(max_length=30)
    dificultad = models.IntegerField()
    duracion_indivudual = models.IntegerField()
  


class Engranes(models.Model):
    Engraneid = models.IntegerField()
    sessionObtained = models.IntegerField()
    number = models.IntegerField()


class Session(models.Model):
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


class Try(models.Model):
    Levelid = models.IntegerField()
    SessionID = models.IntegerField()
    success = models.booleanField() //duda

    
