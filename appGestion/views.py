from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView,CreateView,UpdateView
from .forms import *


# Create your views here.



"""
class ProductoInsertarView(CreateView):
    model=Producto
    fields=["producto_no","descripcion","precio_actual","stock_disponible"]
    success_url=reverse_lazy('producto_base')

class ProductoListarView(ListView):
    model=Producto
    template_name="ventasApp/formulario.html"
    fields=["producto_no","descripcion","precio_actual","stock_disponible"]
    def get_queryset(self):
        return Producto.objects.all()

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
    template='formulario.html'
    return render(request,template,{'formulario':form})

class InsertarView(CreateView):


 
"""
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

        url=opcion+'.html'
        return render(request,url,{'respuesta':listado})

"""
def eliminar(request,opcion,index):
    match opcion:
        case "productos": 
            objeto=Producto.objects.get(id=index)
            objeto.delete()
            listado=Producto.objects.all()
        case "clientes":
            objeto=Cliente.objects.get(id=index)
            objeto.delete()
            listado=Cliente.objects.all()
        case "departamentos":
            objeto=Departamento.objects.get(id=index)
            objeto.delete()
            listado=Departamento.objects.all()
        case "empleados":
            objeto=Empleado.objects.get(id=index)
            objeto.delete()
            listado=Empleado.objects.all()
        case "pedidos":
            objeto=Pedido.objects.get(id=index)
            objeto.delete()
            listado=Pedido.objects.all()
        case "subscripciones":
            objeto=Subscripcion.objects.get(id=index)
            objeto.delete()
            listado=Subscripcion.objects.all()
    
    url=opcion+'.html'
    return render(request,url,{'respuesta':listado})

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
        
