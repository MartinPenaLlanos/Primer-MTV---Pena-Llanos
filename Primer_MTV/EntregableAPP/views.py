from http.client import HTTPResponse
from django.shortcuts import render
from EntregableAPP.models import *
from contextvars import Context
import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.

def clientes(request):
    return render (request, "EntregableAPP/elientes.html")

def empleados(request):
    return render (request, "EntregableAPP/empleados.html")

def inicio(request):
    return render (request, "EntregableAPP/inicio.html")

def cursos(request):
    return render (request, "EntregableAPP/cursos.html")

def estudiantes(request):
    return render (request, "EntregableAPP/estudiantes.html")

def profesores(request):
    return render (request, "EntregableAPP/profesores.html")

def entregables(request):
    return render (request, "EntregableAPP/entregables.html")