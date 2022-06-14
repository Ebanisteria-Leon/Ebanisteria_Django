from products.api.serializer.product_serializers import ProductoSerializers
from products.models import Promocion

from rest_framework import serializers

class PromocionSerializers(serializers.ModelSerializer):
    idProducto = ProductoSerializers(many = True)
    
    class Meta:
        model = Promocion
        fields = '__all__'
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')