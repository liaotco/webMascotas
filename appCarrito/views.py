from django.shortcuts import render, redirect
from appGestion.models import Producto
from appCarrito.carrito import Carrito

# Create your views here.
def pruebas(request):
    return render(request,'pruebas.html')

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

def agregarcarrito(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.agregar(producto)
    return redirect('verCarrito')

def sacar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.sacar(producto)
    return redirect('tienda')

def sacarcarrito(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.sacar(producto)
    return redirect('verCarrito')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('verCarrito')



