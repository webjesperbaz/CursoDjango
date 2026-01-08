from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):        #primera vista
    return HttpResponse("hola wey")

def despedida(request):        #segunda vista

    nombre= "Jesus" #para poder pasarle a la plantilla el valor en el contexto
    apellido= "Perea"
    dia= datetime.now()
    temasDelCurso=["plantillas", "modelos", "formularios", "vistas", "Despliegue"]


    doc_externo= open("C:/Users/perea/Desktop/django/cursoDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")  #cargo documento externo
    plt=doc_externo.read()     #lo abro y lo lee
    doc_externo.close()         #lo cierra  
    plt = Template(plt)         # Convertimos el texto plano en un objeto Template de Django 
    
    ctx = Context({"nombre_persona": nombre, "apellido_persona": apellido, "dia_actual": dia, "temas": temasDelCurso})       #creo el contexto, siempre en diccionario obligatorio aunque esté vacio
    documento = plt.render(ctx)                 #renderizamos el documemto
    return HttpResponse(documento)

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



