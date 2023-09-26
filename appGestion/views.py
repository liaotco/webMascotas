from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView


# Create your views here.

def webGestion(request):
    return render(request,'baseGestion.html')

def cargaForm(request,opcion):
    return render(request,'form_insertar.html',{'respuesta':opcion})
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
    url=opcion+'.html'
    return render(request,url,{'respuesta':listado})

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
            objeto=Subscripcion.objects.all()
            objeto.delete()
    url=opcion+'.html'
    return render(request,url,{'respuesta':objeto})

def insertar(request,opcion):
    match opcion:
        case "productos": 
           
        case "clientes":
           
        case "departamentos":
            
        case "empleados":
            
        case "pedidos":
           
        case "subscripciones":
            
    url=opcion+'.html'
    return render(request,url,{'respuesta':objeto})

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
        
