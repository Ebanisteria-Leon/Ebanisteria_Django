from expense_manager.models import *

from rest_framework import serializers

class PedidosPendientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = PedidosPendiente
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')

    def to_representation(self, instance):
        return {
            'idPedidosPendientes': instance.idPedidosPendientes,

            'fechaPedido': instance.fechaPedido,
            'estadoPedido': instance.estadoPedido,
            
            'estadoPedido': instance.estadoPedido,

            'idProducto': [
                instance.idProducto.idProducto,
                instance.idProducto.nombre,
                instance.idProducto.tiempoProducto,
                instance.idProducto.estadoProducto,
                instance.idProducto.destacado,
                instance.idProducto.valor
            ],

            'idPersona': [
                instance.idPersona.id,
                instance.idPersona.name,
                instance.idPersona.last_name,
                instance.idPersona.email
            ],

            'idComprobantePago': [
                instance.idComprobantePago.idComprobantePago,
                instance.idComprobantePago.nombre
            ],
            'idTipoPago': [
                instance.idTipoPago.idTipoPago,
                instance.idTipoPago.nombre
            ]
        }


class DetallesCompraSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetallesCompra
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')

    def to_representation(self, instance):
        return {
            'idDetallesCompra': instance.idDetallesCompra,
            'cantidad': instance.cantidad,

            'vUnitario': instance.vUnitario,
            'vTotal': instance.vTotal,

            'fechaCompra': instance.fechaCompra,
            
            'comprobante_number': instance.comprobante_number,
            'estadoCompra': instance.estadoCompra,
            
            'idComprobantePago': [
                instance.idComprobantePago.idComprobantePago,
                instance.idComprobantePago.nombre
            ],
            'idTipoPago': [
                instance.idTipoPago.idTipoPago,
                instance.idTipoPago.nombre
            ],

            'idProducto': [
                instance.idProducto.idProducto,
                instance.idProducto.nombre,
                instance.idProducto.descripcion,
                instance.idProducto.valor
            ],

            'idPersona': [
                instance.idPersona.name,
                instance.idPersona.last_name,
                instance.idPersona.email,
                instance.idPersona.direccion,
            ]
        }
        
class ComprobantePagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComprobantePago
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
        
class TipoPagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
