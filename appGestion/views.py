from typing import Any, Dict, Optional
from django import http
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView,CreateView
from .forms import *
from django.urls import reverse_lazy


# Create your views here.



"""
class ProductoInsertarView(CreateView):
    model=Producto
    fields=["producto_no","descripcion","precio_actual","stock_disponible"]
    success_url=reverse_lazy('producto_base')


class ProductoUpdateView(UpdateView):
    model=Producto
    template_name="ventasApp/formulario.html"
    fields=["precio_actual","stock_disponible"]
    success_url=reverse_lazy('producto_base')

"""

def webGestion(request):
    return render(request,'baseGestion.html')

         
def mostrar(request,opcion):
    match opcion:
        case "productos": 
            listado=Producto.objects.all()
        case "clientes":
            listado=Cliente.objects.all()
        case "departamentos":
            listado=Departamento.objects.all()
        case "empleados":
            listado=Empleado.objects.all()
        case "pedidos":
            listado=Pedido.objects.all()
        case "subscripciones":
            listado=Subscripcion.objects.all()
 
    url=opcion+'.html'
    return render(request,url,{'respuesta':listado})


class insertarProducto(CreateView):
        model = Producto
        fields =['nombre','precio','imagen']
        template_name='formulario.html'   
        success_url=reverse_lazy('mostrar' 'productos')   
      

class insertarCliente(CreateView):
        model = Cliente
        fields = ['nombre','localidad','debe','haber','limite_credito']
        template_name='formulario.html'
        success_url=reverse_lazy('mostrar' 'clientes') 
  

class insertarEmpleado(CreateView):
        model = Empleado
        fields = ['apellido','oficio','fecha_alta','salario','comision','telefono','dep']
        template_name='formulario.html'
        success_url=reverse_lazy('mostrar''empleados') 

class insertarDepartamento(CreateView):
        model = Departamento
        fields = ['nombre','localidad']
        template_name='formulario.html'
        success_url=reverse_lazy('mostrar''departamentos') 

class insertarPedido(CreateView):
        model = Pedido
        fields = ['producto','cliente','unidades']
        template_name='formulario.html'
        success_url=reverse_lazy('mostrar''pedidos') 

def eliminarProducto(request,index):
    objeto=Producto.objects.get(id=index)
    objeto.delete()    
    return redirect('mostrar' 'productos')

def eliminarCliente(request,index):
    objeto=Cliente.objects.get(id=index)
    objeto.delete()
    return redirect('mostrar' 'clientes')

def eliminarSubscripcion(request,index):
    objeto=Subscripcion.objects.get(id=index)
    objeto.delete()
    return redirect('mostrar' 'subscripciones')

def eliminarEmpleado(request,index):
    objeto=Empleado.objects.get(id=index)
    objeto.delete()
    return redirect('mostrar' 'empleados')

def eliminarDepartamento(request,index):
    objeto=Departamento.objects.get(id=index)
    objeto.delete()
    return redirect('mostrar' 'departamentos')

def eliminarPedido(request,index):
    objeto=Pedido.objects.get(id=index)
    objeto.delete()
    return redirect('mostrar' 'pedidos')
    

def editarProducto(request,prod_no):
    producto=Producto.objects.get(id=prod_no)
    if request.method == 'POST':
        producto.imagen=request.POST['imagen']
        producto.nombre=request.POST['nombre']
        producto.precio=request.POST['precio']
        producto.save()
        return redirect('verProducto')

    return render(request,'form_editar.html',{'producto':producto})

class ProductoDetailView(DetailView):
        model=Producto
        template_name='detalle.html'
        def get_object(self):
            objeto=self.model.objects.get(id=self.kwargs['pk'])
            return objeto
        
