from django.contrib import admin
from expense_manager.models import *

# Register your models here.

class DetallesAdmin(admin.ModelAdmin):
    list_display = ('idDetallesCompra', 'idPersona', 'fechaCompra')

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('idPedidosPendientes', 'idPersona', 'fechaPedido')


admin.site.register(DetallesCompra, DetallesAdmin)
admin.site.register(PedidosPendiente, PedidosAdmin)
