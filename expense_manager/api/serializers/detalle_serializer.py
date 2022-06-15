from expense_manager.models import *
from products.api.serializer.product_serializers import ProductoSerializers

from rest_framework import serializers

class ListDetallesCompraSerializers(serializers.ModelSerializer):
    idProductos = ProductoSerializers(many = True, read_only = False)

    class Meta:
        model = DetallesCompra
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')


class DetallesCompraSerializers(serializers.ModelSerializer):

    class Meta:
        model = DetallesCompra
        fields = '__all__'
