from django.shortcuts import render, redirect
from appGestion.models import *
from appCarrito.carrito import Carrito
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    productos=Producto.objects.all() #sacamos todos los productos de la tabla
    return render(request,'portada.html')

def tienda(request):
    productos=Producto.objects.all() #sacamos todos los productos de la tabla
    return render(request,'tiendaonline.html',{'productos':productos}) #devolvemos por contexto a la plantilla html la lista de productos de la bd
@login_required
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
contraseña gmail para python
uksx djwg rzsp bjcx

"""
# import necessary packages 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def enviarEmail(request):
# create message object instance 
    msg = MIMEMultipart()
    msgCopy = MIMEMultipart()
    sender="rosalia.otero@gmail.com"
    password = "uksx djwg rzsp bjcx"
    
  # setup the parameters of the message 
    receiver=request.POST["introducir_email"]
    nombre=request.POST["introducir_nombre"]
    mensaje=request.POST["introducir_mensaje"]

    message = f"Hola {nombre}. Gracias por tu solicitud de contacto: {mensaje}, en breve nos pondremos en contacto contigo."
    messageHtml = f"""\
<html>
<head>
</head>
<body>
<div class="contenedor" style="  margin: 0 auto; padding: 1%;">
    <h1>Hola, {nombre}</h1>
    <h4>
        ¿Qué tal estás? Muchas gracias por contactar con nosotros, hemos recibido correctamente el mensaje:
        <div class="mensaje">
            <span>{mensaje}</span>
        </div>
        En breve nos pondremos en contacto contigo de nuevo en el email: <span>{receiver}</span> con la respuesta a tu solicitud.
        <br>
        Un saludo.
    </h4>
</div>

</body>
</html>
"""
    subject="Solicitud de contacto"

    receiverCopy="rosalia.otero@gmail.com"
    messageCopy = f"Se ha recibido una solicitud de contacto de {receiver}, con nombre: {nombre} y con el mensaje: {mensaje}"
    messageCopyHtml = f"""\
<html>
<head>
</head>
<body>
<div class="contenedor" style="  margin: 0 auto; padding: 2%;">
    <h1>Buenos días,</h1>
    <h4>Se ha recibido una solicitud de contacto: <br>    
        
        <div class="mensaje" style="border: 1px solid black; width: 50%;margin: 0 auto;padding: 2%;">
            - Nombre:{nombre}  <br>
            - Email: {receiver} <br>
            - Mensaje: {mensaje} <br>
        </div>
        <br>    
        Un saludo.
    </h4>    
</div>

</body>
</html>
"""
    msgCopy['From']=sender
    msgCopy['To'] = receiverCopy
    msgCopy['Subject'] = subject

    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

# add in the message body 
    msg.attach(MIMEText(messageHtml, 'html'))
    msgCopy.attach(MIMEText(messageCopyHtml, 'html'))

    
#create server 
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
# Login Credentials for sending the mail 
    server.login(sender, password)
    # send the message via the server. 

    server.sendmail(sender, receiver, msg.as_string())
    server.sendmail(sender, receiverCopy, msgCopy.as_string())
    server.quit()
    return redirect('contacto')
   
