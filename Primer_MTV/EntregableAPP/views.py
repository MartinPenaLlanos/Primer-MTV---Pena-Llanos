from http.client import HTTPResponse
from django.shortcuts import render
from EntregableAPP.models import *
from contextvars import Context
import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.


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

    return HTTPResponse(txt2)

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

def curso(self):

    curso = Curso(nombre = "SQL", camada = "101657")
    curso.save()
    doctxt = f"-->Curso: {curso.nombre}  Camada: {curso.camada}"

    return HttpResponse(doctxt)


def familiares(self):

    familiar1 = Familiares(nombre = "Juan", apellido = "Pena", edad = "30", fecha_nac = "1990-09-10")
    familiar2 = Familiares(nombre = "Ignacio", apellido = "Pena", edad = "32", fecha_nac = "1988-08-10")
    familiar3 = Familiares(nombre = "Mariana", apellido = "Pena", edad = "28", fecha_nac = "1992-07-10")

    familiar1.save()
    familiar2.save()
    familiar3.save() 

    texto = f"Familiares Creados: Nombre/s : {familiar1.nombre};{familiar2.nombre};{familiar3.nombre} Apellido/s: {familiar1.apellido};{familiar2.apellido};{familiar3.apellido} Edad/es: {familiar1.edad};{familiar2.edad};{familiar3.edad} \n Fecha/s de Nacimiento: {familiar1.fecha_nac};{familiar2.fecha_nac};{familiar3.fecha_nac}"

    return HttpResponse(texto)