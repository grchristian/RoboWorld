from rest_framework import serializers
from .models import Reto
class RetoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Reto
    fields = ('nombre', 'minutos_jugados')
