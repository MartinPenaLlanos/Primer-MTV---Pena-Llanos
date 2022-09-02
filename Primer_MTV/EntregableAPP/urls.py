
from django.urls import path
from EntregableAPP.views import *

urlpatterns = [
    
    path("clientes/", clientes, name = "clientes"),
    path("empleados/", empleados, name="empleados"),
    path("cursos/", cursos, name="cursos"),
    path("", inicio, name="inicio"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
   
]                 