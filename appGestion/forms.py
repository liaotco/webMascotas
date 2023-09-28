from django import forms 
from .models import *

class formProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields =['nombre','precio','imagen']
        labels = {
            'nombre':'Insertar datos:',
            'precio':'',
            'imagen':''
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'placeholder':'Nombre','class':'form_input'}),
            'precio':forms.TextInput(attrs={'placeholder':'Precio','class':'form_input'}),
            'imagen':forms.TextInput(attrs={'placeholder':'Imagen','class':'form_input'})
        }

class formCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','localidad','debe','haber','limite_credito']
        labels = {
            'nombre':'Insertar datos:',
            'localidad':'',
            'debe':'',
            'haber':'',
            'limite_credito':''
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'placeholder':'Nombre','class':'form_input'}),
            'localidad':forms.TextInput(attrs={'placeholder':'Localidad','class':'form_input'}),
            'debe':forms.TextInput(attrs={'placeholder':'Debe','class':'form_input'}),
            'haber':forms.TextInput(attrs={'placeholder':'Haber','class':'form_input'}),
            'limite_credito':forms.TextInput(attrs={'placeholder':'Crédito','class':'form_input'})
        }

class formEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['apellido','oficio','fecha_alta','salario','comision','telefono','dep']
        labels = {
            'nombre':'Insertar datos:',
            'oficio':'',
            'fecha_alta':'',
            'salario':'',
            'comision':'',
            'telefono':'',
            'dep':''
        }
        widgets = {
            'apellido':forms.TextInput(attrs={'placeholder':'Nombre','class':'form_input'}),
            'oficio':forms.TextInput(attrs={'placeholder':'Oficio','class':'form_input'}),
            'fecha_alta':forms.TextInput(attrs={'placeholder':'Fecha alta','class':'form_input'}),
            'salario':forms.TextInput(attrs={'placeholder':'Salario','class':'form_input'}),
            'comision':forms.TextInput(attrs={'placeholder':'Comision','class':'form_input'}),
            'telefono':forms.TextInput(attrs={'placeholder':'Telefono','class':'form_input'}),
            
        }
class formDepartamento(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre','localidad']
        labels = {
            'nombre':'Insertar datos:',
            'localidad':''            
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'placeholder':'Nombre','class':'form_input'}),
            'localidad':forms.TextInput(attrs={'placeholder':'Localidad','class':'form_input'})            
        }
class formPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto','cliente','unidades']
        labels = {
            'nombre':'Insertar datos:',
            'cliente':'',
            'unidades':''
        }
        widgets = {        
            'unidades':forms.TextInput(attrs={'placeholder':'Unidades','class':'form_input'})
        }