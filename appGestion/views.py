from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView


# Create your views here.

def webGestion(request):
    return render(request,'baseGestion.html')

def cargaForm(request):
    return render(request,'form_insertar.html')
# PRODUCTOS

def mostrarProductos(request):
     productos=Producto.objects.all()
     return render(request,'productos.html',{'productos':productos})


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
"""
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
"""