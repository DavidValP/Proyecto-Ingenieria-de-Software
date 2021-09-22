from django.shortcuts import render, HttpResponse

# Create your views here.
def Contacto(request):
    return render(request, 'Contactos/contacto.html')