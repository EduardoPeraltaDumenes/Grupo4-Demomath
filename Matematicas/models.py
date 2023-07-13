from django.db import models
from django.urls import reverse

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    favorito =[]
    def agregarFavoritos(self, favorito):
        pass

    def realizarComentario(self, comentario):
        pass

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    favorito = []
    def agregarFavoritos(self, favorito):
        pass

    def realizarComentario(self, comentario):
        pass

    def editarPagina(self):
        pass

    def borrarComentario(self, comentario):
        pass

    def crearDemostracion(self, demostracion):
        pass

    def borrarDemostracion(self, demostracion):
        pass

class Demostracion(models.Model):
    titulo = models.CharField(max_length=100)
    explicacion = models.TextField()

    def realizarComentario(self, comentario):
        pass

class Comentario(models.Model):
    texto = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    IDcomentario = models.CharField(max_length=100)
