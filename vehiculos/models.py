from django.db import models

# Create your models here.
#importes de usuarios.models
from usuarios.models import Persona , conductor

# modelos de vehiculos
class vehiculo (models.Model):
    id_conductor = models.ForeignKey(conductor, on_delete=models.CASCADE)
    placa = models.CharField(max_length=20)
    foto_vehiculo = models.ImageField(upload_to='media', null=True, blank=True)
    estado = models.BooleanField(default=True)
    
    
    
    def __str__(self):
        return self.id_conductor.id_persona.name
    
class Referencia_vehiculo (models.Model):
    id_vehiculo = models.ForeignKey(vehiculo, on_delete=models.CASCADE)
    nombre_referencia = models.CharField(max_length=20)
    
    
    
    
    def __str__(self):
        return self.nombre_referencia
    
class Marca_vehiculo (models.Model):
    id_referencia_vehiculo = models.ForeignKey(Referencia_vehiculo, on_delete=models.CASCADE)
    nombre_marca = models.CharField(max_length=20)
    
    
    
    def __str__(self):
        return self.nombre_marca
