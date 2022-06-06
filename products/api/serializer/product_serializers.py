from products.models import Producto
from products.api.serializer.category_serializers import *

from rest_framework import serializers

class ProductoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Producto
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')

    def to_representation(self, instance):
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
            'imagen': instance.imagen,
            'imagen2': instance.imagen2,

            'fechaInicio': instance.fechaInicio,
            'fechaFinalizacion': instance.fechaFinalizacion,

            'estadoProducto': instance.estadoProducto,
            'destacado': instance.destacado,
            'tiempoProducto': instance.tiempoProducto,
            'idCategoria': instance.idCategoria.nombreCategoria
        }
