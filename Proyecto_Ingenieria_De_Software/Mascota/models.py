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
    imagenes = models.ImageField(upload_to='media/mascota_imagenes',null=True, blank=True)

    class Meta:
        verbose_name = 'Perrito'
        verbose_name_plural = 'Perritos'

    def __str__(self):
        return self.nombre