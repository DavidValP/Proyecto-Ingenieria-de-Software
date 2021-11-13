
from django.shortcuts import render, HttpResponse
from Mascota.models import Perrito, PerritoImagenes
# Create your views here.
def Galeria(request):

    mascotas = Perrito.objects.all()#importamos todos los registros de perritos

    return render(request, 'Galerias/galeria.html', {'mascotas':mascotas})