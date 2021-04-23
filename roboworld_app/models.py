from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Usuario(models.Model):
    #UserioId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    
class Reto(models.Model):
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)


    minutos_jugados = models.IntegerField(null=True)
    minimo = models.IntegerField(null=True)
    maximo = models.IntegerField(null=True)
    repeticion_niveles = models.IntegerField(null=True)
    engranes = models.IntegerField(null=True)
    duracion_promedio = models.IntegerField(null=True)
    success_promedio = models.IntegerField(null=True)
    a_que_nivel_llego = models.IntegerField(null=True)
    sesion_iniciada_dia=models.IntegerField(null=True)
    sesion_iniciada_mes=models.IntegerField(null=True)




class Article(models.Model):
    headline = models.CharField(max_length=255)
    article = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)


class Level(models.Model):
    #Nivelid = models.AutoField(primary_key=True)
    level_number = models.IntegerField()
    enemigo = models.CharField(max_length=30)
    dificultad = models.IntegerField()
    duracion_indivudual = models.IntegerField()
    
  


class Engranes(models.Model):
    sessionObtained = models.IntegerField()
    number = models.IntegerField()


class Sesion(models.Model):
    #SessionId = models.IntegerField()
   # UserID = models.IntegerField()
    started = models.IntegerField()
    ended = models.IntegerField()
  
   



class Recompensas(models.Model):
    
    engranes_necesarios = models.IntegerField()
    top_score_global = models.IntegerField()
    top_five = models.IntegerField()


class Prueba(models.Model):
    #Levelid = models.IntegerField()
    SesionID = models.IntegerField()
    success = models.BooleanField() 

    
