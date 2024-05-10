from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nom = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nom

class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula + ' - ' + self.marca + " " + self.model
