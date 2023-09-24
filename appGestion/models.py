from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.CharField(max_length=5,primary_key=True)
    nombre = models.CharField(max_length=50,blank=False)
    precio = models.FloatField()
    imagen=models.CharField(max_length=254,blank=True)
    def __str__(self):
        return self.nombre


class Subscripcion(models.Model):
    nombre=models.CharField(max_length=50,blank=False,default=True)
    email = models.CharField(max_length=50,blank=False)
    def __str__(self):
        return self.email

class Departamento(models.Model):
    dep_no=models.PositiveSmallIntegerField(primary_key=True)
    dnombre=models.CharField(max_length=14,blank=False)
    localidad=models.CharField(max_length=30,blank=False)


class Empleado(models.Model):
    emp_no=models.PositiveSmallIntegerField(primary_key=True)
    apellido=models.CharField(max_length=8,blank=False)
    oficio=models.CharField(max_length=10,blank=False)
    director=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    fecha_alta=models.DateField()
    salario=models.DecimalField(max_digits=8,decimal_places=2)
    comision=models.DecimalField(max_digits=8,decimal_places=2)
    dep_no=models.ForeignKey(Departamento,on_delete=models.CASCADE,default='1',blank=True)
    telefono=models.CharField(max_length=14,blank=False)

class Cliente(models.Model):
    cliente_no=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=25,blank=False)
    localidad=models.CharField(max_length=14,blank=False)
    vendedor_no=models.ForeignKey(Empleado,on_delete=models.CASCADE,blank=True)
    debe=models.DecimalField(max_digits=8,decimal_places=2)
    haber=models.DecimalField(max_digits=8,decimal_places=2)
    limite_credito=models.DecimalField(max_digits=8,decimal_places=2)

class Pedido(models.Model):
    pedido_no=models.PositiveSmallIntegerField(primary_key=True)
    producto_no = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente_no=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    unidades=models.SmallIntegerField()
    fecha_pedido=models.DateField()

