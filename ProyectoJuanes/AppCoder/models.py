from django.contrib.auth.decorators import login_required
from django.db import models

from django.contrib.auth.models import User
# from django.db.models.fields.files import ImageField

# Create your models here.
class Auto(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"

class Moto(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"

class Camion(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"


class Vender(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"

class Busqueda(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    
    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"


# class Avatar(models.Model):
    
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    
    

