from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView
from .forms import *


# Create your views here.

def webGestion(request):
    return render(request,'baseGestion.html')

def cargaForm(request,opcion):  
    match opcion:
        case "productos": 
            form=formProducto()            
        case "clientes":
            form=formCliente()
        case "departamentos":
            form=formDepartamento()
        case "empleados":
            form=formEmpleado()
        case "pedidos":
            form=formPedido()
    url='form_'+opcion+'.html'
    return render(request,url,{'formulario':form})
            
# PRODUCTOS

"""
def insertarProducto(request):
    if request.method == 'POST':
        var_id=request.POST['id']
        var_imagen=request.POST['imagen']
        var_nombre=request.POST['nombre']
        var_precio=request.POST['precio']
        producto=Producto.objects.create(id=var_id,
                                     imagen=var_imagen,
                                     nombre=var_nombre,
                                     precio=var_precio)
        return redirect('verProducto')
    return mostrarProductos(request)

    def eliminarProducto(request,prod_no):
    producto=Producto.objects.get(id=prod_no)
    producto.delete()    
    return redirect('verProducto')

    
"""
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
 
    return render(request,'tablasgeneral.html',{'respuesta':listado})

def eliminar(request,opcion,index):
    match opcion:
        case "productos": 
            objeto=Producto.objects.get(id=index)
            objeto.delete()
        case "clientes":
            objeto=Cliente.objects.get(id=index)
            objeto.delete()
        case "departamentos":
            objeto=Departamento.objects.get(id=index)
            objeto.delete()
        case "empleados":
            objeto=Empleado.objects.get(id=index)
            objeto.delete()
        case "pedidos":
            objeto=Pedido.objects.get(id=index)
            objeto.delete()
        case "subscripciones":
            objeto=Subscripcion.objects.get(id=index)
            objeto.delete()
    
    return render(request,'tablasgeneral.html',{'respuesta':objeto})

def insertar(request,opcion):
    if request.method == 'POST':
        match opcion:
            case "productos": 
                form = formProducto(request.POST)
                if form.is_valid():
                    form.save()
                listado=Producto.objects.all()
            case "clientes":
                form = formCliente(request.POST)
                if form.is_valid():
                    form.save()
                listado=Cliente.objects.all()
            case "departamentos":
                form = formDepartamento(request.POST)
                if form.is_valid():
                    form.save()
                listado=Departamento.objects.all()
            case "empleados":
                form = formEmpleado(request.POST)
                if form.is_valid():
                    form.save()
                listado=Empleado.objects.all()
            case "pedidos":
                form = formPedido(request.POST)
                if form.is_valid():
                    form.save()
                listado=Pedido.objects.all()

    return render(request,'tablasgeneral.html',{'respuesta':listado})

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
        
