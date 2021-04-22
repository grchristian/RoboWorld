from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    #UserioId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    
class Reto(models.Model):
    Userid = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    minutos_jugados = models.IntegerField()
    minimo = models.IntegerField()
    maximo = models.IntegerField()
    repeticion_niveles = models.IntegerField()
    engranes = models.IntegerField()
    duracion_promedio = models.IntegerField()
    success_promedio = models.IntegerField()
    a_que_nivel_llego = models.IntegerField()
    sesion_iniciada_dia=models.IntegerField()
    sesion_iniciada_mes=models.IntegerField()
    decoracion = model.IntegerField()
   
    


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
    usa_decoraciones = models.ForeignKey(Reto, on_delete=models.CASCADE)
    engranes_necesarios = models.IntegerField()
    top_score_global = models.IntegerField()
    top_five = models.IntegerField()


class Prueba(models.Model):
    #Levelid = models.IntegerField()
    SesionID = models.IntegerField()
    success = models.BooleanField() 

    
