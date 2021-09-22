from django.shortcuts import render, HttpResponse

# Create your views here.
def Galeria(request):
    return render(request, 'Galerias/galeria.html')
