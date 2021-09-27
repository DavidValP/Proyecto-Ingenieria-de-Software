from django.shortcuts import render

# Create your views here.
def Mascota(request):
    return render(request, 'Mascota/mascota.html')