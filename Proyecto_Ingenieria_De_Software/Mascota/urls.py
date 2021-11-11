from django.urls import path
from Mascota import views

urlpatterns = [
    path('', views.Mascota, name='Mascota'),
]