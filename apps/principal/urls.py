from django.contrib import admin
from django.urls import path
from .views import Home,Registro,Info,Mapas,Principal,Juegos


urlpatterns =[
    path('', Home, name="Home"), 
    path('Registro.html/', Registro, name="Registro"),
    path('principal.html/', Principal, name="Principal"),
    path('informacion.html/', Info, name="Info"),
    path('mapas.html/', Mapas, name="Mapas"),
    path('juegos.html/', Juegos, name="Juegos"),
]