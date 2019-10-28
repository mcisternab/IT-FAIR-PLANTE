from django.contrib import admin
from django.urls import path
from .views import Home,Registro,Info,Mapas,Inicio


urlpatterns =[
    path('', Home, name="Home"), 
    path('Registro.html/', Registro, name="Registro"),
    path('informacion.html/', Info, name="Info"),
    path('mapas.html/', Mapas, name="Mapas"),
    path('iniciosesion.html/', Inicio, name="Inicio"),
]