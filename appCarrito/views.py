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

class insertarSubscripcion(CreateView):
    model=Subscripcion
    fields=["nombre","email"]
    success_url=reverse_lazy('inicio')

        # import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json 

def enviarEmail(request):
    if request.method == 'POST':
        var_nombre=request.POST['introducir_nombre']
        var_email=request.POST['introducir_email']
        var_mensaje=request.POST['introducir_mensaje']
        
        sender = 'rosalia.otero@gmail.com'
        port = 25 
        smtp_server = "smtp.gmail.com"
        login = "rosalia.otero@gmail.com" 
        password = "Bzt1zu1g_l"
        sender_email = "rosalia.otero@gmail.com" 
        receiver_email = var_email,sender_email
        message = MIMEMultipart("")
        message["Subject"] = "My Pet Shop: Confirmación solicitud información."
        message["From"] = sender_email
        message["To"] = receiver_email

    # write the text/plain part
        text = """\
            Hola {{var_nombre}},
            Hemos recibido tu solicitud de contacto con los siguientes datos:
            - Nombre: {{var_nombre}}
            - Email: {{var_email}}
            - Mensaje: {{var_mensaje}}
            En breve nos pondremos en contacto contigo. 
            Muchas gracias, un saludo.
        """
    # write the HTML part
        message.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(message['From'], password)
        server.sendmail(message['From'], message['To'], message.as_string())
        server.quit()
    return redirect('contacto')        


"""
        html = 
        <html>
            <body>
            <p>Hola {{var_nombre}},<br>
            Hemos recibido tu solicitud de contacto con los siguientes datos: </p>
            <p> - Nombre: {{var_nombre}}</p>
            <p> - Email: {{var_email}}</p>
            <p> - Mensaje: {{var_mensaje}}</p>
            <p>     En breve nos pondremos en contacto contigo. 
                                    Muchas gracias, un saludo.</p>
            </body>
        </html>
    """