from django.db import models
from django.contrib.auth.models import User
from django.conf import settings




'''
'''
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
'''




class Reto(models.Model):
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
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
    #id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    #Levelid = models.IntegerField()
    SesionID = models.IntegerField()
    success = models.BooleanField() 

    
