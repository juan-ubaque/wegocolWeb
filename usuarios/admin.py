from django.contrib import admin
#importamos los modelos que vamos a administrar
from .models import Persona , conductor , Location
# Register your models here.

admin.site.register(Persona)

admin.site.register(conductor)

admin.site.register(Location)