from products.api.serializer.product_serializers import ProductoSerializers
from products.models import Producto, Promocion

from rest_framework import serializers

class PromocionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Promocion
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')

    def to_representation(self, instace):
        return [
            
        ]