from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from EntregableAPP.forms import ClientesForm, EmpleadosForm

# Create your views here.

def cliente(request):

    
    nombre = request.POST.get("nombre")
    dni = request.POST.get("dni")
    categoria = request.POST.get("categoria")
    cliente = cliente(nombre=nombre, dni=dni, categoria=categoria)
    cliente.save()
    cliente=cliente(nombre="curso creado en el ejemplo", dni=0, categoria="black")
    print("CREANDO CLIENTE")
    cliente.save()
    
    texto=f"cliente creado"
    return HttpResponse(texto)

def clientes_black(request):
    return render (request, "EntregableAPP/clientes_black.html")

def clientes_gold(request):
    return render (request, "EntregableAPP/clientes_gold.html")

def clientes_platinum(request):
    return render (request, "EntregableAPP/clientes_platinum.html")

def empleados(request):
    return render (request, "EntregableAPP/empleados.html")

def inicio(request):
    return render (request, "EntregableAPP/inicio.html")

def busqueda(request):
    return render (request, "EntregableAPP/busqueda.html")



def clientes(request):
    if request.method=="POST":
        form=ClientesForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            dni=informacion["dni"]
            categoria=informacion["categoria"]
            curso=Clientes(nombre=nombre, dni=dni, categoria=categoria)
            curso.save()
            return render (request, "EntregableAPP/inicio.html")

    else:
        formulario=ClientesForm()
        return render (request, "EntregableAPP/clientes.html", {"formulario":formulario})


#def profeFormulario(request):
#
#    if request.method=="POST":
#        form= ProfeForm(request.POST)
#        if form.is_valid():
#            info= form.cleaned_data
#            nombre= info["nombre"]
#            apellido= info["apellido"]
#            email= info["email"]
#            profesion= info["profesion"]
#            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
#            profe.save()
#            return render (request, "EntregableAPP/inicio.html", {"mensaje":"Profesor creado"})
#    else:
#        form= ProfeForm()
#    return render(request, "EntregableAPP/profeForm.html", {"formulario":form})



def buscar(request):
    if request.GET["dni"]:

        dni=request.GET["dni"]
        clientes=Clientes.objects.filter(dni=dni)
        return render(request, "EntregableAPP/resultados_busqueda.html", {"clientes":clientes})
    else:
        return render(request, "EntregableAPP/busqueda.html", {"mensaje":"Ingrese un numero de DNI"})
    
    return HttpResponse(respuesta)

