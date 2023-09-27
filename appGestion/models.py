from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50,blank=False)
    precio = models.FloatField()
    imagen=models.CharField(max_length=254,blank=True)
    def __str__(self):
        return self.nombre


class Subscripcion(models.Model):
    nombre=models.CharField(max_length=50,blank=False,default=True)
    email = models.CharField(max_length=50,blank=False)
    fecha_alta=models.DateField(auto_now=True)
    def __str__(self):
        return self.email

class Departamento(models.Model):
    nombre=models.CharField(max_length=14,blank=False)
    localidad=models.CharField(max_length=30,blank=False)


class Empleado(models.Model):
    apellido=models.CharField(max_length=8,blank=False)
    oficio=models.CharField(max_length=10,blank=False)
    fecha_alta=models.DateField()
    salario=models.DecimalField(max_digits=8,decimal_places=2)
    comision=models.DecimalField(max_digits=8,decimal_places=2)
    dep=models.ForeignKey(Departamento,on_delete=models.CASCADE,default='1',blank=True)
    telefono=models.CharField(max_length=14,blank=False)

class Cliente(models.Model):
    nombre=models.CharField(max_length=25,blank=False)
    localidad=models.CharField(max_length=14,blank=False)
    debe=models.DecimalField(max_digits=8,decimal_places=2)
    haber=models.DecimalField(max_digits=8,decimal_places=2)
    limite_credito=models.DecimalField(max_digits=8,decimal_places=2)

class Pedido(models.Model):   
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    unidades=models.SmallIntegerField()
    fecha_pedido=models.DateField(auto_now=True)