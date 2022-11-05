#importe de rest_framework
from rest_framework import serializers

#importe de los modelos
from .models import Location

class LocationUpdateSerializer(serializers.ModelSerializer):
    #Atributos que se van a serializar
    class Meta:
        model = Location
        fields = ('persona','token','lat', 'lon')
    