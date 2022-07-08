from distutils.command.upload import upload
from pickle import TRUE
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models
from autoslug import AutoSlugField

# Create your models here.

#Mapeo URM

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta: 
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    categorias = models.ForeignKey(CategoriaProd, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to = "tienda", null = True, blank = True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "Productos"
        
    def __str__(self):
        return self.nombre
