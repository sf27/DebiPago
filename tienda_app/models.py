#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.forms import ERROR_MESSAGE



class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, error_messages={'required': 'Por favor ingrese el nombre'})
    descripcion = models.TextField(help_text='Describe la categoria de articulos', error_messages={'required': 'Por favor ingrese la descripción'})
    fecha_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(help_text='Describe el articulo')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad =models.IntegerField()
    imagen = models.ImageField(upload_to='articulo', verbose_name='Imágen')
    fecha_registro = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.nombre
    
class Comentario(models.Model):
    contenido = models.TextField(help_text='Ingresa tu comentario')
    fecha_registro = models.DateTimeField(auto_now=True)
    articulo = models.ForeignKey(Articulo)
    usuario = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.articulo.nombre
    
class Compra(models.Model):
    cantidad = models.IntegerField()
    precio_articulo = models.DecimalField(max_digits=10, decimal_places=2)#precio_articulo en el momento de la compra
    status = models.CharField(max_length=10, unique=False)
    fecha_registro = models.DateTimeField(auto_now=True)
    articulo = models.ForeignKey(Articulo)
    usuario = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.articulo.nombre + "_" + str(self.cantidad) + "_" + str(self.fecha_registro)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    