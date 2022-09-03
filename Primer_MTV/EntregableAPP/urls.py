from django.urls import path
from EntregableAPP.views import *

urlpatterns = [
    
    path("clientes/", clientes, name = "clientes"),
    path("empleados/", empleados, name="empleados"),
    path("empleadosform/", empleadosForm, name="empleadosForm"),
    path("clientesblack/", clientes_black, name="clientes_black"),
    path("", inicio, name="inicio"),
    path("clientesgold/", clientes_gold, name="clientes_gold"),
    path("clientesplatinum/", clientes_platinum, name="clientes_platinum"),
    path("busqueda/", busqueda, name="busqueda"),
    path("clientesform/", clientesForm, name="clientesForm"),
    path("nuevosusuariosform/", nuevos_usuariosForm, name="nuevosusuariosForm"),
           
]                 