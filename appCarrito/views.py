from django.shortcuts import render, redirect
from appGestion.models import Producto
from appCarrito.carrito import Carrito

# Create your views here.

def inicio(request):
    productos=Producto.objects.all() #sacamos todos los productos de la tabla
    return render(request,'portada.html')

def tienda(request):
    productos=Producto.objects.all() #sacamos todos los productos de la tabla
    return render(request,'tiendaonline.html',{'productos':productos}) #devolvemos por contexto a la plantilla html la lista de productos de la bd

def verCarrito(request):
    return render(request,'carrito.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def agregar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.agregar(producto)
    return redirect('tienda')

def sacar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.sacar(producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('tienda')



