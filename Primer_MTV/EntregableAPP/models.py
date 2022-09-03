from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    categoria = models.CharField(max_length=40)
     
    def __str__(self):
      return self.nombre+" "+str(self.dni)

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido


    