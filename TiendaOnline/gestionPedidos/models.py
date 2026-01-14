from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tfno=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la sección es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)
    # def __str__(self):
    #     return f"El nombre es {self.nombre}, la sección es {self.seccion} y el precio es {self.precio}"     #para que se vea como cadena de texto si es llamada para ver objetos de la base de datos

class Pedidos(models.Model):
    nombre=models.CharField()
    fecha=models.DateField()
    entregado=models.BooleanField()



