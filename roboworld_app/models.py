from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

class Engranes(models.Model):
    engrames_id = models.IntegerField(null=True)
    #id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    sessionObtained = models.IntegerField(null=True)
    number = models.IntegerField(null=True)


class Reto(models.Model):
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    minutos_jugados = models.IntegerField(null=True)
    minimo = models.IntegerField(null=True)
    maximo = models.IntegerField(null=True)
    repeticion_niveles = models.IntegerField(null=True)
    engranes = models.ForeignKey(Engranes, on_delete=models.CASCADE,null=True)
    duracion_promedio = models.IntegerField(null=True)
    success_promedio = models.IntegerField(null=True)
    a_que_nivel_llego = models.IntegerField(null=True)
    sesion_iniciada_dia=models.IntegerField(null=True)
    sesion_iniciada_mes=models.IntegerField(null=True)

class Perfil(models.Model):
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    genero = models.CharField(max_length=1, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Level(models.Model):
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    #Nivelid = models.AutoField(primary_key=True)
    level_number = models.IntegerField(null=True)
    enemigo = models.CharField(max_length=30, null=True)
    dificultad = models.IntegerField(null=True)
    duracion_indivudual = models.IntegerField(null=True)





class Sesion(models.Model):
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    #SessionId = models.IntegerField()
   # UserID = models.IntegerField()
    started = models.IntegerField(null=True)
    ended = models.IntegerField(null=True)


class Recompensas(models.Model):
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    engranes_necesarios = models.IntegerField(null=True)
    top_score_global = models.IntegerField(null=True)
    top_five = models.IntegerField(null=True)


class Prueba(models.Model):
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    #Levelid = models.IntegerField()
    SesionID = models.IntegerField(null=True)
    success = models.BooleanField(null=True) 

    
