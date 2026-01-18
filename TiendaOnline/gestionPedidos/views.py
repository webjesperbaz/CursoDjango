from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. Vistas:

def busqueda_productos(request):
    return render(request, "busqueda_productos.html" )

def buscar(request):
    if request.GET["prd"]:
        
        mensaje= "Articulo buscado es : %r" %request.GET["prd"]         #informacion que le viene desde el formulario
    
    else:
        mensaje="No has introducido nada."
        
    return HttpResponse(mensaje)