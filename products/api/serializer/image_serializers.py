from products.models import ImagenesProductos

from rest_framework import serializers

class ImagenesProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImagenesProductos
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
