from django.urls import path
from Galeria import views

urlpatterns = [
    path('', views.Galeria, name='Galeria'),
]