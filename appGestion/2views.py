from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView,DetailView #modulo de django para mostrar listas

# Create your views here.

def webGestion(request):
    productos=Producto.objects.all()
    return render(request,'webGestion.html',{'productos':productos})

# PRODUCTOS
def productoListView(request):
    productos=Producto.objects.all()  
    return render(request,'productos.html',{"prod":productos})


def insertarProducto(request):
    var_producto_no= request.POST['producto_no']
    var_descripcion=request.POST['descripcion']
    var_precio_actual=request.POST['precio_actual']
    var_stock_disponible =request.POST['stock_disponible']

    producto=Producto.objects.create(producto_no=var_producto_no,
                                     descripcion=var_descripcion,
                                     precio_actual=var_precio_actual,
                                     stock_disponible=var_stock_disponible)
    return redirect('/verProducto')

def eliminarProducto(request,prod_no):
    producto=Producto.objects.get(producto_no=prod_no)
    producto.delete()    
    return redirect('/verProducto')



"""
def insertar(request,numprod):
    producto=Producto(producto_no=numprod,
                      descripcion="inserto",
                      precio_actual=25.50,
                      stock_disponible=10)
    
    producto.save()
    return redirect('/inicio')

def eliminar(request,numprod):
    producto=Producto(producto_no=numprod)
    producto.delete()
    return redirect('/inicio')

def modificar(request,numprod):
    producto=Producto(producto_no=numprod)
    producto.descripcion="holaaaaaaaaa"
    producto.stock_disponible=2
    producto.precio_actual=1
    producto.save()
    return redirect('/inicio')
"""