from django.contrib import admin
from expense_manager.models import *

# Register your models here.

class DetallesAdmin(admin.ModelAdmin):
    list_display = ('idDetallesCompra', 'idPersona', 'fechaCompra')

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('idPedidosPendientes' 'fechaPedido')

class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('idComprobantePago', 'nombre')

class TipoPagoAdmin(admin.ModelAdmin):
    list_display = ('idTipoPago', 'nombre')

admin.site.register(DetallesCompra, DetallesAdmin)
admin.site.register(PedidosPendiente, PedidosAdmin)
admin.site.register(ComprobantePago, ComprobanteAdmin)
admin.site.register(TipoPago, TipoPagoAdmin)
