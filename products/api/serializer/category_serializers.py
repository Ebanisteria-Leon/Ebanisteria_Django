from products.models import Categoria

from rest_framework import serializers

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')