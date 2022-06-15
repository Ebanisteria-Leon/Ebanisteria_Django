from expense_manager.models import *
from products.api.serializer.product_serializers import ProductoSerializers
from users.api.serializers import UserListSerializers

from rest_framework import serializers


class ListPedidosPendientesSerializers(serializers.ModelSerializer):
    idProducto = ProductoSerializers(many = True, read_only = False)
    idPersona = UserListSerializers(many = True, read_only = False)

    class Meta:
        model = PedidosPendiente
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')

class PedidosPendientesSerializers(serializers.ModelSerializer):

    class Meta:
        model = PedidosPendiente
        fields = '__all__'
