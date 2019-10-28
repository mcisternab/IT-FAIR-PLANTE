from django.contrib import admin
from django.urls import path
from .views import Home,Registro,Info,Formulario,Inicio


urlpatterns =[
    path('', Home, name="Home"), 
    path('Registro.html/', Registro, name="Registro"),
    path('informacion.html/', Info, name="Info"),
    path('formulario.html/', Formulario, name="Formulario"),
    path('iniciosesion.html/', Inicio, name="Inicio"),
]