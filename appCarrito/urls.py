from django.contrib import admin
from django.urls import path
from .views import inicio,agregar_producto,sacar_producto,limpiar_carrito,nosotros,contacto,verCarrito,tienda,agregarcarrito,sacarcarrito
from .views import insertarSubscripcion, enviarEmail
""""
path('',pruebas,name='pruebas'),
"""
urlpatterns = [
    path('',inicio,name='inicio'),
    path('tienda',tienda,name='tienda'),
    path('agregar/<int:prod_id>',agregar_producto,name='agregar'),
    path('agregarcarrito/<int:prod_id>',agregarcarrito,name='agregarcarrito'),
    path('sacar/<int:prod_id>',sacar_producto,name='sacar'),
    path('sacarcarrito/<int:prod_id>',sacarcarrito,name='sacarcarrito'),
    path('limpiar/',limpiar_carrito,name='limpiar'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('verCarrito/',verCarrito, name='verCarrito'),
    path('insertarSubscripcion/',insertarSubscripcion.as_view(), name='insertarSubscripcion'),
    path('enviarEmail/',enviarEmail, name='enviarEmail')
]
