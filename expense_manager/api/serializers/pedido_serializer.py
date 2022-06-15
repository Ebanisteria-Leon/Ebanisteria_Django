from expense_manager.models import *
from products.api.serializer.product_serializers import ProductoSerializers

from rest_framework import serializers


class ListPedidosPendientesSerializers(serializers.ModelSerializer):

    class Meta:
        model = PedidosPendiente
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')

class PedidosPendientesSerializers(serializers.ModelSerializer):

    class Meta:
        model = PedidosPendiente
        fields = '__all__'
