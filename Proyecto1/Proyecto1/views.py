from django.http import HttpResponse
from datetime import datetime

def saludo(request):        #primera vista
    return HttpResponse("hola wey")

def despedida(request):        #segunda vista
    return HttpResponse("aaaaaaadios")

def dameFecha (request):            #tercera vista, esta será dinamica ya que la hora ira cambiando
    fecha_actual= datetime.now()
    documento= f"<h1>Fecha y hora actuales:</h1> {fecha_actual}"
    return HttpResponse(documento)

def calculaEdad (request, edad, agno):    #cuarta vista, esta recivirá parametros
    # edadActual= 18
    periodo= int(agno)-2025
    edadFutura= int(edad) + periodo
    documento= f"<h1>En el año: {agno} tendras {edadFutura}</h1> "

    return HttpResponse (documento)



