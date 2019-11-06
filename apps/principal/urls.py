from django.contrib import admin
from django.urls import path, re_path, include
from .views import Home,Registro,Info,Mapas,Principal,Juegos,login,Perfil

urlpatterns =[
    path('', login, name="login"), 
    path('Registro.html/', Registro, name="Registro"),
    path('principal.html/', Principal, name="Principal"),
    path('informacion.html/', Info, name="Info"),
    path('mapas.html/', Mapas, name="Mapas"),
    path('juegos.html/', Juegos, name="Juegos"),
    path('perfil.html/', Perfil, name="Perfil"),
]