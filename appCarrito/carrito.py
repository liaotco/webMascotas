#clase para leer datos de sesion y de inicio
from appGestion.models import Producto

class Carrito:
    def __init__(self,request): #leemos los datos de inicio sesión, en este caso sesion y request
#inicializamos 
        self.request=request  #los pasamos a variables que controlemos nosotros
        self.session=request.session
        #necesario verificar si el carrito ya existe de una visita anterior, 
        # si existe mostrar datos
        carrito=self.session.get('carrito') ##coge el carrito que tenemos en sesión para usarla en una variable 
        if not carrito:
            self.session['carrito']={}    # si no existe inicializar a 0
            self.carrito=self.session['carrito']
        else:
            self.carrito=carrito 
          
           
#funcionalidades que le vamos a dar a nuestro carro de la compra
    def agregar(self,producto):
            id=str(producto.id) #cargamos el id y lo convertimos en string para usar como clave del diccionario carrito
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "id": producto.id,   
                    "nombre": producto.nombre,
                    "precio": producto.precio,
                    "cantidad":1,
                    "subtotal": producto.precio
                }
            else:
                self.carrito[id]['cantidad']+=1
                self.carrito[id]['subtotal']+=producto.precio
            self.guardar_carrito()

    def sacar(self,producto):
            id=str(producto.id) #cargamos el id y lo convertimos en string para usar como clave del diccionario carrito
            if id in self.carrito.keys():
                self.carrito[id]['cantidad']-=1
                self.carrito[id]['subtotal']-=producto.precio
                if self.carrito[id]['cantidad']==0:
                    #opcion 2 eliminar  -> self.eliminar(producto) eliminar producto de la lista 
                       del self.carrito[id]
            self.guardar_carrito()

    def guardar_carrito(self):
                self.session['carrito']=self.carrito
                self.session.modified=True
            
#Limpiar carrito 

    def limpiar(self):
        self.session['carrito']={}    # si no existe inicializar a 0
        self.session.modified=True