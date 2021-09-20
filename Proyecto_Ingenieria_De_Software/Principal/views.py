from django.shortcuts import render, HttpResponse

def Principal(request):
    return render(request, 'Principal/index.html')

