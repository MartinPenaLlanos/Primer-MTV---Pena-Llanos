from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    categoria = models.CharField(max_length=40)
     
    def __str__(self):
      return self.nombre+" "+str(self.dni)+" "+self.categoria

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.email+" "+self.puesto


class Nuevos_Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.email+" "+self.password


    