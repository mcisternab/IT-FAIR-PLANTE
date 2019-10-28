from django.db import models

# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    fnacimiento = models.DateField()
    comentarios = models.CharField(max_length=50)

class Juego (models.Model):
    idjuego = models.CharField(max_length=12, primary_key=True)
    puntos = models.IntegerField()
    intentos = models.IntegerField()

class Partidas (models.Model):
    idjuego = models.CharField(max_length=12, primary_key=True)
    gpartida = models.CharField(max_length=20)

class Registro(models.Model):
    nombreusuario = models.CharField(max_length=20, primary_key=True)
    contrasena = models.CharField(max_length=20)

