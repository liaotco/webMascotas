from django import forms 
from .models import *

class formProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields =['nombre','precio','imagen']

class formCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','localidad','debe','haber','limite_credito']

class formEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['apellido','oficio','fecha_alta','salario','comision','telefono','dep']

class formDepartamento(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre','localidad']
class formPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto','cliente','unidades']