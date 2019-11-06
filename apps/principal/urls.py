from django.contrib import admin
from django.urls import path, re_path, include
from .views import Home,Registro,Info,Mapas,Principal,Juegos,login,Perfil,Complete,Confirm,Done,Email,Form

urlpatterns =[
    path('', login, name="login"), 
    path('Registro.html/', Registro, name="Registro"),
    path('principal.html/', Principal, name="Principal"),
    path('informacion.html/', Info, name="Info"),
    path('mapas.html/', Mapas, name="Mapas"),
    path('juegos.html/', Juegos, name="Juegos"),
    path('perfil.html/', Perfil, name="Perfil"),
    path('password_reset_complete.html/', Complete, name="Complete"),
    path('password_reset_confirm.html/', Confirm, name="Confirm"),
    path('password_reset_done.html/', Done, name="Done"),
    path('password_reset_email.html/', Email, name="Email"),
    path('password_reset_form.html/', Form, name="Form"),
]