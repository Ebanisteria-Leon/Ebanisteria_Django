from expense_manager.models import *

from rest_framework import serializers

class PedidosPendientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = PedidosPendiente
        exclude = ('estadoCreacion', 'fechaCreacion',
                   'fechaModificacion', 'fechaEliminacion')

    def to_representation(self, instance):
        return {
            'idPedidosPendientes': instance.idPedidosPendientes,

            'fechaPedido': instance.fechaPedido,
            'estadoPedido': instance.estadoPedido,

            'idProducto': [
                instance.idProducto.nombre,
                instance.idProducto.descripcion
            ],

            'idPersona': [
                instance.idPersona.id,
                instance.idPersona.name,
                instance.idPersona.last_name,
                instance.idPersona.email
            ]
        }


class DetallesCompraSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetallesCompra
        exclude = ('estadoCreacion', 'fechaCreacion',
                   'fechaModificacion', 'fechaEliminacion')

    def to_representation(self, instance):
        return {
            'idDetallesCompra': instance.idDetallesCompra,
            'cantidad': instance.cantidad,

            'vUnitario': instance.vUnitario,
            'vTotal': instance.vTotal,

            'fechaCompra': instance.fechaCompra,
            'TipoPago': instance.TipoPago,

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
