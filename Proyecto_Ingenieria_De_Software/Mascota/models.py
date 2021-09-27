from django.db import models

# Create your models here.

class Tamaño(models.Model):
    tamaño = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Perrito(models.Model):
    nombre = models.CharField(max_length=20, null=True, blank=True)
    raza = models.CharField(max_length=40)
    color_pelaje = models.CharField(max_length=20, null=True, blank=True)
    tamaño = models.ForeignKey(Tamaño, on_delete=models.CASCADE)    
    edad = models.IntegerField(null=True, blank=True)