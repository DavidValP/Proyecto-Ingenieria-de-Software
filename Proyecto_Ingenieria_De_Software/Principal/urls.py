from django.urls import path
from Principal import views

urlpatterns = [
    path('', views.Principal, name='Principal'),
   
]
