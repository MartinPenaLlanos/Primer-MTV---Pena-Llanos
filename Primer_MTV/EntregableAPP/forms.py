from django import forms

class ClientesForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    categoria = forms.CharField(max_length=50)
    
class EmpleadosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    puesto = forms.CharField(max_length=50)

class Nuevos_UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
