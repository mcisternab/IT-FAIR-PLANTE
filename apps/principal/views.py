from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'principal/index.html')

def Registro(request):
    return render(request, 'principal/Registro.html')

def Info(request):
    return render(request, 'principal/informacion.html')

def Formulario(request):
    return render(request, 'principal/formulario.html')

def Inicio(request):
    return render(request, 'principal/iniciosesion.html')