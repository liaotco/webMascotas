from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', webGestion,name='webGestion'),     
    path('insertarProducto',insertarProducto.as_view(),name='insertarProducto'),
    path('insertarCliente',insertarCliente.as_view(),name='insertarCliente'),
    path('insertarEmpleado',insertarEmpleado.as_view(),name='insertarEmpleado'),
    path('insertarDepartamento',insertarDepartamento.as_view(),name='insertarDepartamento'),
    path('insertarPedido',insertarPedido.as_view(),name='insertarPedido'),
    path('eliminarProducto/<int:index>',eliminarProducto,name='eliminarProducto'),  
    path('eliminarCliente/<int:index>',eliminarCliente,name='eliminarCliente'),  
    path('eliminarSubscripcion/<int:index>',eliminarSubscripcion,name='eliminarSubscripcion'),  
    path('eliminarEmpleado/<int:index>',eliminarEmpleado,name='eliminarEmpleado'),  
    path('eliminarDepartamento/<int:index>',eliminarDepartamento,name='eliminarDepartamento'),  
    path('eliminarPedido/<int:index>',eliminarPedido,name='eliminarPedido'),  
    path('verProducto/',mostrarProductos, name='verProducto'),
    path('verSubscripcion/',mostrarSubscripciones, name='verSubscripcion'),
    path('verCliente/',mostrarClientes, name='verCliente'),
    path('verDepartamento/',mostrarDepartamentos, name='verDepartamento'),
    path('verEmpleado/',mostrarEmpleados, name='verEmpleado'),
    path('verPedido/',mostrarPedidos, name='verPedido'),
    path('editarProducto/<pk>',editarProducto.as_view(),name='editarProducto'),
    path('editarPedido/<pk>',editarPedido.as_view(),name='editarPedido'),
    path('editarCliente/<pk>',editarCliente.as_view(),name='editarCliente'),
    path('editarEmpleado/<pk>',editarEmpleado.as_view(),name='editarEmpleado'),
    path('editarDepartamento/<pk>',editarPedido.as_view(),name='editarDepartamento'),
    path('productoDetalle/<pk>',ProductoDetailView.as_view(),name='productoDetalle'),
    path('clienteDetalle/<pk>',ClienteDetailView.as_view(),name='clienteDetalle'),
    path('empleadoDetalle/<pk>',EmpleadoDetailView.as_view(),name='empleadoDetalle'),
     ]



