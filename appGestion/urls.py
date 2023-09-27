from django.contrib import admin
from django.urls import path
from .views import webGestion, editarProducto,ProductoDetailView,cargaForm, mostrar,InsertarView

"""
from .views import mostrarSubscripciones,mostrarClientes,mostrarDepartamentos,mostrarEmpleados,mostrarPedidos,insertarProducto,mostrarProductos,eliminarProducto,insertar

path('gestionTienda', webGestion,name='webGestion'),
    path('insertarProducto/',insertarProducto,name='insertarProducto'),  
  
        path('verProducto/',mostrarProductos, name='verProducto'),
    path('verSubscripcion/',mostrarSubscripciones, name='verSubscripcion'),
    path('verCliente/',mostrarClientes, name='verCliente'),
    path('verDepartamento/',mostrarDepartamentos, name='verDepartamento'),
    path('verEmpleado/',mostrarEmpleados, name='verEmpleado'),
    path('verPedido/',mostrarPedidos, name='verPedido'),
       path('eliminarProducto/<int:prod_no>',eliminarProducto,name='eliminarProducto'),
          
"""
urlpatterns = [
    path('', webGestion,name='webGestion'),

    path('eliminar/<str:opcion><int:index>',mostrar,name='mostrar'),  
    path('editarProducto/<int:prod_no>',editarProducto,name='editarProducto'),
    path('cargaForm/<str:opcion>', cargaForm,name='cargaForm'), 
    path('productoDetalle/<pk>',ProductoDetailView.as_view(),name='productoDetalle'),
    path('mostrar/<str:opcion>',mostrar,name='mostrar'),  
    path("insertarView",InsertarView.as_view(),name='insertar')
     ]



