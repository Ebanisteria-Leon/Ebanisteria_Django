from expense_manager.models import *
from products.api.serializer.product_serializers import ProductoSerializers

from rest_framework import serializers

class ComprobantePagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComprobantePago
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
        
class TipoPagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
