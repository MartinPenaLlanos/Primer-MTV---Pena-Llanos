
from django.urls import path
from EntregableAPP.views import *

urlpatterns = [
    
    path("curso/", curso),
    path("saludo/", saludo),
    path("vista2/", vista2),
    path("template/", template),
    path("template2/", template2),
    path('nombre/<nombre>', nombre),
    path("fecha/", fecha),
    path("familiares/", familiares),
    
]
