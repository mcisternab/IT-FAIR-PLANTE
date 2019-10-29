from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'principal/index.html')

def Registro(request):
    return render(request, 'principal/Registro.html')

def Principal(request):
    return render(request, 'principal/principal.html')

def Info(request):
    return render(request, 'principal/informacion.html')

def Mapas(request):
    return render(request, 'principal/mapas.html')

def Juegos(request):
    return render(request, 'principal/juegos.html')


