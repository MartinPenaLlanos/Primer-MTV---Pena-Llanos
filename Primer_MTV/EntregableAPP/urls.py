
from django.urls import path
from EntregableAPP.views import *

urlpatterns = [
    
    path("curso/", curso, name="curso"),
    path("saludo/", saludo, name = "saludo"),
    path("vista2/", vista2, name = "vista2"),
    path("template/", template, name = "template"),
    path("template2/", template2, name="template2"),
    path('nombre/<nombre>', nombre, name = "nombre"),
    path("fecha/", fecha, name = "fecha"),
    path("familiares/", familiares, name = "familiares"),
    
]
