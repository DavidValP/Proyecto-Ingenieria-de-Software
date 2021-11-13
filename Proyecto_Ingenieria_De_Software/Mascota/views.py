from django.shortcuts import render
from Mascota.models import Perrito, PerritoImagenes
from django.db.models import Q

# Create your views here.
def Mascota(request):

    id_perrito = request.GET.get('mascota')#nombre del perrito solicitado

    imagenes_perrito = PerritoImagenes.objects.all()#todas las imagenes de los perros

    
    perrito = Perrito.objects.get(pk=id_perrito)#datos del perrito seleccionado


    return render(request, 'Mascota/mascota.html', {'perrito':perrito, 'imagenes':imagenes_perrito, 'nombre_perrito':id_perrito} )