from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from EntregableAPP.forms import CursoForm, ProfeForm

# Create your views here.

def curso(request):

    
    nombre = request.POST.get("nombre")
    comision = request.POST.get("comision")
    curso = Curso(nombre=nombre, comision=comision)
    curso.save()
    curso=Curso(nombre="curso creado en el ejemplo", comision=0)
    print("CREANDO CURSO")
    curso.save()
    
    texto=f"curso creado"
    return HttpResponse(texto)

def clientes(request):
    return render (request, "EntregableAPP/clientes.html")

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



def cursos(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "EntregableAPP/inicio.html")

    else:
        formulario=CursoForm()
        return render (request, "AppCoder/cursos.html", {"formulario":formulario})


def profeFormulario(request):

    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "EntregableAPP/inicio.html", {"mensaje":"Profesor creado"})
    else:
        form= ProfeForm()
    return render(request, "EntregableAPP/profeForm.html", {"formulario":form})


def busquedaComision(request):
    return render(request, "EntregableAPP/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:

        comision=request.GET["comision"]
        #traeme de la base, TODOS los cursos que tengan esa comision
        cursos=Curso.objects.filter(comision=comision)
        return render(request, "EntregableAPP/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "EntregableAPP/busquedaComision.html", {"mensaje":"CHE! Ingresa una comision"})
    
    return HttpResponse(respuesta)
