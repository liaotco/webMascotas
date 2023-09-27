from django.contrib import admin
from django.urls import path
from .views import webGestion,insertarProducto, eliminarProducto,editarProducto,mostrarProductos,ProductoDetailView,cargaForm
from .views import mostrarSubscripciones,mostrarClientes,mostrarDepartamentos,mostrarEmpleados,mostrarPedidos
"""
 
path('gestionTienda', webGestion,name='webGestion'),

  
"""
urlpatterns = [
    path('', webGestion,name='webGestion'),
    path('verProducto/',mostrarProductos, name='verProducto'),
    path('verSubscripcion/',mostrarSubscripciones, name='verSubscripcion'),
    path('verCliente/',mostrarClientes, name='verCliente'),
    path('verDepartamento/',mostrarDepartamentos, name='verDepartamento'),
    path('verEmpleado/',mostrarEmpleados, name='verEmpleado'),
    path('verPedido/',mostrarPedidos, name='verPedido'),
     path('insertarProducto/',insertarProducto,name='insertarProducto'),
    path('eliminarProducto/<int:prod_no>',eliminarProducto,name='eliminarProducto'),
    path('editarProducto/<int:prod_no>',editarProducto,name='editarProducto'),
    path('cargaForm/', cargaForm,name='cargaForm'), 
    path('productoDetalle/<pk>',ProductoDetailView.as_view(),name='productoDetalle'),
   
]



