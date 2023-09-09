from django.contrib import admin
from django.urls import path
from .views import webGestion,insertarProducto, eliminarProducto,editarProducto,mostrarProductos,ProductoDetailView,cargaForm

"""
 
path('gestionTienda', webGestion,name='webGestion'),

  
"""
urlpatterns = [
    path('', webGestion,name='webGestion'),
    path('verProducto/',mostrarProductos, name='verProducto'),
    path('insertarProducto/',insertarProducto,name='insertarProducto'),
    path('eliminarProducto/<int:prod_no>',eliminarProducto,name='eliminarProducto'),
    path('editarProducto/<int:prod_no>',editarProducto,name='editarProducto'),
    path('cargaForm/', cargaForm,name='cargaForm'), 
    path('productoDetalle/<pk>',ProductoDetailView.as_view(),name='productoDetalle'),
 
]



