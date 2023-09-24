from django.shortcuts import render, redirect
from appGestion.models import *
from appCarrito.carrito import Carrito
from django.views.generic import CreateView
from django.urls import reverse_lazy

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

def agregarcarrito(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.agregar(producto)
    return redirect('verCarrito')

def sacar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.sacar(producto)
    return redirect('verCarrito')



def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('verCarrito')

class insertarSubscripcion(CreateView):
    model=Subscripcion
    fields=["nombre","email"]
    success_url=reverse_lazy('inicio')

        # import the necessary components first


"""
contraseña gmal para python
uksx djwg rzsp bjcx

"""
# import necessary packages 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def enviarEmail(request):
# create message object instance 
    msg = MIMEMultipart()
    sender="rosalia.otero@gmail.com"
    password = "uksx djwg rzsp bjcx"
    
  # setup the parameters of the message 
    receiver=request.POST["introducir_email"]
    nombre=request.POST["introducir_nombre"]
    message = "Hola {{nombre}}. Gracias por tu solicitud de contacto, en breve nos pondremos en contacto contigo."
    subject="Solicitud de contacto"

    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
# add in the message body 
    msg.attach(MIMEText(message, 'plain'))
#create server 
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
# Login Credentials for sending the mail 
    server.login(msg['From'], password)
    # send the message via the server. 
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
   
