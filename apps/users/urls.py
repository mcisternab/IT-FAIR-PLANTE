from django.contrib import admin
from django.urls import path, re_path, include
from .views import Home,Info,Mapas,Principal,Juegos,login,Perfil
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

urlpatterns =[
    path('', login, name="login"), 
    path('principal.html/', Principal, name="Principal"),
    path('informacion.html/', Info, name="Info"),
    path('mapas.html/', Mapas, name="Mapas"),
    path('juegos.html/', Juegos, name="Juegos"),
    path('perfil.html/', Perfil, name="Perfil"),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_forms.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),
]