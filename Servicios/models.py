from distutils.command.upload import upload
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.

class Servicios(models.Model):
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 50)
    imagen = models.ImageField(upload_to = 'servicios')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo