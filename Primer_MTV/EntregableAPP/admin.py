from django.contrib import admin
from .models import Clientes, Empleado, Nuevos_Usuarios

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Empleado)
admin.site.register(Nuevos_Usuarios)

