from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView,CreateView,UpdateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# VIEWS MOSTRAR DATOS
def webGestion(request):
    return render(request,'baseGestion.html')

         
def mostrarProductos(request):
     listado=Producto.objects.all()
     return render(request,'productos.html',{'respuesta':listado})

def mostrarSubscripciones(request):
     listado=Subscripcion.objects.all()
     return render(request,'subscripciones.html',{'respuesta':listado})

def mostrarClientes(request):
     listado=Cliente.objects.all()
     return render(request,'clientes.html',{'respuesta':listado})

def mostrarDepartamentos(request):
     listado=Departamento.objects.all()
     return render(request,'departamentos.html',{'respuesta':listado})

def mostrarEmpleados(request):
     listado=Empleado.objects.all()
     return render(request,'empleados.html',{'respuesta':listado})
     

def mostrarPedidos(request):
     listado=Pedido.objects.all()
     return render(request,'pedidos.html',{'respuesta':listado})

# VIEWS INSERTAR DATOS

class insertarProducto(CreateView):
        model = Producto
        form_class=formProducto
        template_name='formulario.html'   
        success_url=reverse_lazy('verProducto')       

class insertarCliente(CreateView):
        model = Cliente
        form_class=formCliente
        template_name='formulario.html'
        success_url=reverse_lazy('verCliente') 

class insertarEmpleado(CreateView):
        model = Empleado
        form_class=formEmpleado
        template_name='formulario.html'
        success_url=reverse_lazy('verEmpleado') 

class insertarDepartamento(CreateView):
        model = Departamento
        form_class=formDepartamento
        template_name='formulario.html'
        success_url=reverse_lazy('verDepartamento') 

class insertarPedido(CreateView):
        model = Pedido
        form_class=formPedido
        template_name='formulario.html'
        success_url=reverse_lazy('verPedido') 

# VIEWS ELIMINAR DATOS
def eliminarProducto(request,index):
    objeto=Producto.objects.get(id=index)
    objeto.delete()    
    return redirect('verProducto')

def eliminarCliente(request,index):
    objeto=Cliente.objects.get(id=index)
    objeto.delete()
    return redirect('verCliente')

def eliminarSubscripcion(request,index):
    objeto=Subscripcion.objects.get(id=index)
    objeto.delete()
    return redirect('verSubscripcion')

def eliminarEmpleado(request,index):
    objeto=Empleado.objects.get(id=index)
    objeto.delete()
    return redirect('verEmpleado')

def eliminarDepartamento(request,index):
    objeto=Departamento.objects.get(id=index)
    objeto.delete()
    return redirect('verDepartamento')

def eliminarPedido(request,index):
    objeto=Pedido.objects.get(id=index)
    objeto.delete()
    return redirect('verPedido')
    
# VIEWS EDITAR DATOS
class editarProducto(UpdateView):
        model = Producto
        form_class=formProducto
        template_name='form_editar.html'   
        success_url=reverse_lazy('verProducto')  

class editarCliente(UpdateView):
        model = Cliente
        form_class=formCliente
        template_name='form_editar.html'   
        success_url=reverse_lazy('verCliente')  

class editarDepartamento(UpdateView):
        model = Departamento
        form_class=formDepartamento
        template_name='form_editar.html'   
        success_url=reverse_lazy('verDepartamento')  

class editarEmpleado(UpdateView):
        model = Empleado
        form_class=formEmpleado
        template_name='form_editar.html'   
        success_url=reverse_lazy('verEmpleado')  

class editarPedido(UpdateView):
        model = Pedido
        form_class=formPedido
        template_name='form_editar.html'   
        success_url=reverse_lazy('verPedido')  

#VIEWS DETALLES 
class ProductoDetailView(DetailView):
        model=Producto
        template_name='detalleProducto.html'
        def get_object(self):
            objeto=self.model.objects.get(id=self.kwargs['pk'])
            return objeto      

class ClienteDetailView(DetailView):
        model=Cliente
        template_name='detalleCliente.html'
        def get_object(self):
            objeto=self.model.objects.get(id=self.kwargs['pk'])
            return objeto
        
        
class EmpleadoDetailView(DetailView):
        model=Empleado
        template_name='detalleEmpleado.html'
        def get_object(self):
            objeto=self.model.objects.get(id=self.kwargs['pk'])
            return objeto
        
#CREAR ARCHIVO PARA DESCARGA

import django_excel as excel
from datetime import datetime

def guardarArchivo(request,opcion):
    export = []

    match opcion:
          
        case 'clientes':
                   # Se agregan los encabezados de las columnas

                export.append(['id','Nombre','Localidad','Debe','Haber','Límite de crédito',])

                # Se obtienen los datos de la tabla o model y se agregan al array

                results = Cliente.objects.all()
                for result in results:

        # ejemplo para dar formato a fechas, estados (si/no, ok/fail) o
        # acceder a campos con relaciones y no solo al id

                        export.append([result.pk,result.nombre,result.localidad,result.debe,result.haber,result.limite_credito])

        case 'departamentos':
                export.append(['id','Nombre','Localidad',])
                results = Departamento.objects.all()
                for result in results:
                        export.append([result.pk,result.nombre,result.localidad])
        case 'empleados':
                export.append(['id','Apellido','Oficio','Fecha de alta','Salario','Comisión','Teléfono','Departamento',])
                results = Empleado.objects.all()
                for result in results:
                        export.append([result.pk,result.apellido,result.oficio,result.fecha_alta,result.salario,result.comision,result.telefono,result.dep])
        case 'pedidos':
                export.append(['id','producto','cliente','unidades',])
                results = Pedido.objects.all()
                for result in results:
                        export.append([result.pk,result.producto,result.cliente,result.unidades])
        case 'productos':             
                export.append(['id','Nombre','Precio','Imagen',  ])
                results = Producto.objects.all()
                for result in results:
                        export.append([result.pk,result.nombre,result.precio,result.imagen])
        case 'subscripciones': 
                export.append(['id','Nombre','Email','Fecha de alta',  ])
                results = Subscripcion.objects.all()
                for result in results:
                        export.append([result.pk,result.nombre,result.email,result.fecha_alta])
   
 # Obtenemos la fecha para agregarla al nombre del archivo
    today    = datetime.now()
    strToday = today.strftime("%Y%m%d")

  # se transforma el array a una hoja de calculo en memoria
    sheet = excel.pe.Sheet(export)
      # se devuelve como "Response" el archivo para que se pueda "guardar"
    # en el navegador, es decir como hacer un "Download"
    return excel.make_response(sheet, "xlsx", file_name="listado-"+opcion+strToday+".xlsx")