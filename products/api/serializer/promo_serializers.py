from products.api.serializer.product_serializers import ProductoSerializers
from products.models import Promocion

from rest_framework import serializers


class ListPromocionSerializers(serializers.ModelSerializer):
    idProducto = ProductoSerializers(many = True, read_only = False)

    class Meta:
        model = Promocion
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')

class PromocionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Promocion
        fields = '__all__'