from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from EntregableAPP.forms import ClientesForm, EmpleadosForm, Nuevos_UsuariosForm

# Create your views here.

#def cliente(request):
#
#    
#    nombre = request.POST.get("nombre")
#    dni = request.POST.get("dni")
#    categoria = request.POST.get("categoria")
#    cliente = cliente(nombre=nombre, dni=dni, categoria=categoria)
#    cliente.save()
#    cliente=cliente(nombre="curso creado en el ejemplo", dni=0, categoria="black")
#    print("CREANDO CLIENTE")
#    cliente.save()
#    
#    texto=f"cliente creado"
#    return HttpResponse(texto)

def clientes_black(request):
    return render (request, "EntregableAPP/clientes_black.html")

def clientes_gold(request):
    return render (request, "EntregableAPP/clientes_gold.html")

def clientes_platinum(request):
    return render (request, "EntregableAPP/clientes_platinum.html")

def clientes(request): 
    return render (request, "EntregableAPP/clientes.html")

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


def clientesForm(request):

    if request.method=="POST":
        form= ClientesForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            dni = info["dni"]
            categoria = info["categoria"]
            cliente= Clientes(nombre=nombre, dni=dni, categoria=categoria)
            cliente.save()
            return render (request, "EntregableAPP/inicio.html", {"mensaje":"Cliente creado"})
    else:
        form= ClientesForm()
    return render(request, "EntregableAPP/clientesForm.html", {"formulario":form})




def empleados(request):
    if request.method=="POST":
        form=EmpleadosForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            empleado=Empleado(nombre=nombre, apellido=apellido, email=email)
            empleado.save()
            return render (request, "EntregableAPP/inicio.html")

    else:
        formulario=EmpleadosForm()
        return render (request, "EntregableAPP/empleados.html", {"formulario":formulario})


def empleadosForm(request):

    if request.method=="POST":
        form= EmpleadosForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            puesto = info["puesto"]	    	
            empleado= Empleado(nombre=nombre, apellido=apellido, email=email, puesto=puesto)
            empleado.save()
            return render (request, "EntregableAPP/inicio.html", {"mensaje":"Empleado creado"})
    else:
        form= EmpleadosForm()
    return render(request, "EntregableAPP/empleadosForm.html", {"formulario":form})



def nuevosusuarios(request):
    if request.method=="POST":
        form=Nuevos_UsuariosForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            password=informacion["password"]
            usuario=Nuevos_Usuarios(nombre=nombre, apellido=apellido, email=email, password=password)
            usuario.save()
            return render (request, "EntregableAPP/inicio.html")

    else:
        formulario=Nuevos_UsuariosForm()
        return render (request, "EntregableAPP/nuevosusuariosForm.html", {"formulario":formulario})


def nuevos_usuariosForm(request):

    if request.method=="POST":
        form= Nuevos_UsuariosForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            password = info["password"]	    	
            usuario= Nuevos_Usuarios(nombre=nombre, apellido=apellido, email=email, password=password)
            usuario.save()
            return render (request, "EntregableAPP/inicio.html", {"mensaje":"Usuario creado"})
    else:
        form= Nuevos_UsuariosForm()
    return render(request, "EntregableAPP/nuevosusuariosForm.html", {"formulario":form})






########################################################################################################################################
def busqueda(request):
    if request.GET["dni"]:

        dni=request.GET["dni"]
        clientes=Clientes.objects.filter(dni=dni)
        return render(request, "EntregableAPP/resultados_busqueda.html", {"clientes":clientes})
    else:
        return render(request, "EntregableAPP/busqueda.html", {"mensaje":"Ingrese un numero de DNI"})
    
    return HttpResponse(respuesta)

