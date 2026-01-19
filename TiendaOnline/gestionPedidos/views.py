from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here. Vistas:

def busqueda_productos(request):
    return render(request, "busqueda_productos.html" )

def buscar(request):
    if request.GET["prd"]:
        
        # mensaje= "Articulo buscado es : %r" %request.GET["prd"]         #informacion que le viene desde el formulario
        producto= request.GET["prd"]

        articulos= Articulos.objects.filter(nombre__icontains= producto)    #busca consulta con sql, lo que recoja del formulario, y (nombre__icontrains= producto) buscará todo lo que en Articulos contenga en nombre esa palabra.

        return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})


    else:
        mensaje="No has introducido nada."
        
    return HttpResponse(mensaje)