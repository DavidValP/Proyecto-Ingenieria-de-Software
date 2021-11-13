from django.db import models

# Create your models here.

class Tamaño(models.Model):
    tamaños = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'Tamaño'
        verbose_name_plural = 'Tamaños'

    def __str__(self):
        return self.tamaños


class Perrito(models.Model):
    nombre = models.CharField(max_length=20, null=True, blank=True)
    raza = models.CharField(max_length=40)
    color_pelaje = models.CharField(max_length=20, null=True, blank=True)
    tamaño = models.ForeignKey(Tamaño, on_delete=models.CASCADE)    
    edad = models.IntegerField(null=True, blank=True)
    portada = models.ImageField(upload_to='portada',null=True,blank=True)

    class Meta:
        verbose_name = 'Perrito'
        verbose_name_plural = 'Perritos'

    def __str__(self):
        return self.nombre

class PerritoImagenes(models.Model):
    perrito = models.ForeignKey(Perrito, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="perritos", null=True, blank=True)

<<<<<<< HEAD
=======


>>>>>>> origin/main
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
