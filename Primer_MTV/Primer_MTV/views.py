from contextvars import Context
import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from EntregableAPP.models import Curso
 
#####################################################################################################


def saludo(request):
    return HttpResponse("Hola Mundo de Django - Coder")

def vista2(request):
    return HttpResponse("Esta es otra vista")

def fecha(request):
    dia = datetime.datetime.now()

    txt = f"Hoy es <br> {dia}"

    return HttpResponse(txt)

def nombre(self, nombre):
    txt2 = f"Mi nombre es <br><br> {nombre}"

    return HttpResponse(txt2)

def template(self):
    
    plantilla = loader.get_template("templates.html")

    documento = plantilla.render()

    return HttpResponse(documento)

def template2(self):
    nom = "Martin"
    ap = "Pena"
    lista_notas = [6,7,2,7,8,3,1,9,10,9,3,7,2,7,4]

    diccionario = {"nombre": nom, "apellido": ap, "hoy":datetime.datetime.now(), "notas": lista_notas}
    
    plantilla = loader.get_template("templates2.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)     



#####################################################################################################