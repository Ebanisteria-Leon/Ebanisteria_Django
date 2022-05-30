from products.models import Producto
from products.api.serializer.category_serializers import *
from products.api.serializer.image_serializers import *

from rest_framework import serializers


class ProductoSerializers(serializers.ModelSerializer):
    idCategoria = CategoriaSerializers(many = True, read_only = True)
    idImagenes = ImagenesProductoSerializers(many = True, read_only = True)

    class Meta:
        model = Producto
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')

    def validate_category(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError(
                'Debe ingresar una Categoria de Producto')

        return value

    def validate_image(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError(
                'Debe ingresar una Imagen de Producto')

        return value

    def validate(self, data):
        if 'idCategoria' not in data.keys():
            raise serializers.ValidationError({
                'idCategoria': 'Debe ingresar una Categoria de Producto'
            })

        if 'idImagenes' not in data.keys():
            raise serializers.ValidationError({
                'idImagenes': 'Debe ingresar una Imagen de Producto'
            })

        return data

    """def to_representation(self, instance):
        return {
            'idProducto': instance.idProducto,
            'nombre': instance.nombre,
            
            'descripcion': instance.descripcion,
            'valor': instance.valor,
            'alto': instance.alto,
            'largo': instance.largo,
            'ancho': instance.ancho,
            'color': instance.color,
            'calificacion': instance.calificacion,
            
            'fechaInicio': instance.fechaInicio,
            'fechaFinalizacion': instance.fechaFinalizacion,
            
            'estadoProducto': instance.estadoProducto,
            'idCategoria': instance.idCategoria,
            'idImagenes': instance.idImagenes
        }"""


class ProductoRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
