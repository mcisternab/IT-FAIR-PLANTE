from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe el usuario
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('principal.html')
    
    
        

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


# Create your views here.

def Home(request):# Creamos el formulario de autenticación vacío
    return render(request, 'principal/principal.html')

def Principal(request):
    if request.user.is_authenticated:
       return render(request, 'principal/principal.html')
    else:
        return redirect('/login')

def Info(request):
    if request.user.is_authenticated:
        return render(request, 'principal/informacion.html')
    else:
        return redirect('/login')

def Mapas(request):
    if request.user.is_authenticated:
        return render(request, 'principal/mapas.html')
    else:
        return redirect('/login')

def Juegos(request):
    if request.user.is_authenticated:
        return render(request, 'principal/juegos.html')
    else:
        return redirect('/login')
    
def Cuestionario(request):
    if request.user.is_authenticated:
        return render(request, 'principal/cuestionario.html')
    else:
        return redirect('/login')

def Perfil(request):
    if request.user.is_authenticated:
        return render(request, 'users/perfil.html')
    else:
        return redirect('/login')

def Administracion(request):
    if request.user.is_superuser == "true":
        return redirect('administracion.html')



