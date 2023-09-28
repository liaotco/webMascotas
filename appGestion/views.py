from typing import Any, Dict, Optional
from django import http
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView,CreateView,UpdateView
from .forms import *
from django.urls import reverse_lazy


# Create your views here.


# VIEWS MOSTRAR DATOS
def webGestion(request):
    return render(request,'baseGestion.html')

         
def mostrarProductos(request):
     listado=Producto.objects.all()
     return render(request,'productos.html',{'respuesta':listado})

def mostrarSubscripciones(request):
     listado=Subscripcion.objects.all()
     return render(request,'subscripciones.html',{'respuesta':listado})

def mostrarClientes(request):
     listado=Cliente.objects.all()
     return render(request,'clientes.html',{'respuesta':listado})

def mostrarDepartamentos(request):
     listado=Departamento.objects.all()
     return render(request,'departamentos.html',{'respuesta':listado})

def mostrarEmpleados(request):
     listado=Empleado.objects.all()
     return render(request,'empleados.html',{'respuesta':listado})

def mostrarPedidos(request):
     listado=Pedido.objects.all()
     return render(request,'pedidos.html',{'respuesta':listado})

# VIEWS INSERTAR DATOS

class insertarProducto(CreateView):
        model = Producto
        form_class=formProducto
        template_name='formulario.html'   
        success_url=reverse_lazy('verProducto')       

class insertarCliente(CreateView):
        model = Cliente
        form_class=formCliente
        template_name='formulario.html'
        success_url=reverse_lazy('verCliente') 

class insertarEmpleado(CreateView):
        model = Empleado
        form_class=formEmpleado
        template_name='formulario.html'
        success_url=reverse_lazy('verEmpleado') 

class insertarDepartamento(CreateView):
        model = Departamento
        form_class=formDepartamento
        template_name='formulario.html'
        success_url=reverse_lazy('verDepartamento') 

class insertarPedido(CreateView):
        model = Pedido
        form_class=formPedido
        template_name='formulario.html'
        success_url=reverse_lazy('verPedidos') 

# VIEWS ELIMINAR DATOS
def eliminarProducto(request,index):
    objeto=Producto.objects.get(id=index)
    objeto.delete()    
    return redirect('verProductos')

def eliminarCliente(request,index):
    objeto=Cliente.objects.get(id=index)
    objeto.delete()
    return redirect('verClientes')

def eliminarSubscripcion(request,index):
    objeto=Subscripcion.objects.get(id=index)
    objeto.delete()
    return redirect('verSubscripciones')

def eliminarEmpleado(request,index):
    objeto=Empleado.objects.get(id=index)
    objeto.delete()
    return redirect('verEmpleados')

def eliminarDepartamento(request,index):
    objeto=Departamento.objects.get(id=index)
    objeto.delete()
    return redirect('verDepartamentos')

def eliminarPedido(request,index):
    objeto=Pedido.objects.get(id=index)
    objeto.delete()
    return redirect('verPedidos')
    
# VIEWS EDITAR DATOS
class editarProducto(UpdateView):
        model = Producto
        form_class=formProducto
        template_name='form_editar.html'   
        success_url=reverse_lazy('verProducto')  

class editarCliente(UpdateView):
        model = Cliente
        form_class=formCliente
        template_name='form_editar.html'   
        success_url=reverse_lazy('verCliente')  

class editarDepartamento(UpdateView):
        model = Departamento
        form_class=formDepartamento
        template_name='form_editar.html'   
        success_url=reverse_lazy('verDepartamento')  

class editarEmpleado(UpdateView):
        model = Empleado
        form_class=formEmpleado
        template_name='form_editar.html'   
        success_url=reverse_lazy('verEmpleado')  

class editarPedido(UpdateView):
        model = Pedido
        form_class=formPedido
        template_name='form_editar.html'   
        success_url=reverse_lazy('verPedido')  

#VIEWS DETALLES 
class ProductoDetailView(DetailView):
        model=Producto
        template_name='detalle.html'
        def get_object(self):
            objeto=self.model.objects.get(id=self.kwargs['pk'])
            return objeto        

class ClienteDetailView(DetailView):
        model=Cliente
        template_name='detalle.html'
        def get_object(self):
            objeto=self.model.objects.get(id=self.kwargs['pk'])
            return objeto
        
class EmpleadoDetailView(DetailView):
        model=Empleado
        template_name='detalle.html'
        def get_object(self):
            objeto=self.model.objects.get(id=self.kwargs['pk'])
            return objeto
        
