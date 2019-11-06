from django.contrib import admin
from django.urls import path, re_path, include
from .views import Home,Registro,Info,Mapas,Principal,Juegos,login
from django.contrib.auth.views import  PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy 

urlpatterns =[
    path('', login, name="login"), 
    path('Registro.html/', Registro, name="Registro"),
    path('principal.html/', Principal, name="Principal"),
    path('informacion.html/', Info, name="Info"),
    path('mapas.html/', Mapas, name="Mapas"),
    path('juegos.html/', Juegos, name="Juegos"),
    path('reset/password_reset', PasswordResetView ,{'template_name': 'registration/password_reset_form.html',
        'email_template_name':'registration/password_reset_email.html'}, 
        name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView, {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView, {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
    ),
    path('reset/done', PasswordResetCompleteView, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
]