from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', webGestion,name='webGestion'),  
    path('editarProducto/<int:prod_no>',editarProducto,name='editarProducto'),
    path('productoDetalle/<pk>',ProductoDetailView.as_view(),name='productoDetalle'),
    path('mostrar/<str:opcion>',mostrar,name='mostrar'),  
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

     ]



