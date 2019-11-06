"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from apps.users import views
from django.contrib.auth.views import  PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy 

urlpatterns = [
    path('',include('apps.principal.urls')),
    # Sección para usuarios
    path('registro', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('admin/', admin.site.urls),
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