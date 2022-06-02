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
                instance.idProducto.descripcion,
                instance.idProducto.valor
            ],

            'idPersona': [
                instance.idPersona.id,
                instance.idPersona.name,
                instance.idPersona.last_name,
                instance.idPersona.email
            ],
            
            'idComprobantePago': instance.nombre,
            'idTipoPago': instance.nombre
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
            
            'idComprobantePago': instance.nombre,
            'idTipoPago': instance.nombre,

            'idProducto': [
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
