from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos     #importo la clase clientes  

# Register your models here.


#clase para ver los campos que quiera y añadir un buscador en la tabla Clientes
class LoQueQuieroQueSeVea(admin.ModelAdmin):
    list_display=("nombre","direccion", "tfno")         #se verá en el panel de admonistracion estos campos
    search_fields=("nombre", "tfno")                    #se añadirá un buscador por esos 

#clase para ver un filtro y filtrar por el campo que desee, los Articulos:
class FiltroArticulos(admin.ModelAdmin):
    list_filter=("seccion",)

#clase para filtrar los pedidos por fecha:
class PedidosFiltroFecha(admin.ModelAdmin):
    list_display=("nombre", "fecha")
    list_filter=("nombre", "fecha")                     #filtro
    date_hierarchy=("fecha")                            #filtro por barra de meses arriba
    
admin.site.register(Clientes, LoQueQuieroQueSeVea)
admin.site.register(Articulos, FiltroArticulos)
admin.site.register(Pedidos, PedidosFiltroFecha)

