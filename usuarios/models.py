from django.db import models

# Create your models here.
class Persona (models.Model):
    generos = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    
    id_persona = models.AutoField(primary_key=True)
    referido = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=generos, default='M')
    cc = models.CharField(max_length=20)
    foto_persona = models.ImageField(upload_to='media', null=True, blank=True)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class conductor (models.Model):
    id_conductor = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    licencia = models.CharField(max_length=20)
    foto_licencia = models.ImageField(upload_to='media', null=True, blank=True)
    foto_conductor = models.ImageField(upload_to='media', null=True, blank=True)
    estado = models.BooleanField(default=True)
    antecedentes = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.id_persona.name