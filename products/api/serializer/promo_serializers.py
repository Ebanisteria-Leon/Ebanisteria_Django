from products.models import Promocion

from rest_framework import serializers

class PromocionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
    
    def to_representation(self, instance):
        return {
            'idPromocion': instance.idPromocion,
            'nombre': instance.nombre,
            
            'valorDescuento': instance.valorDescuento,
            'productoExtra': instance.productoExtra,
            
            'fechaInicio': instance.fechaInicio,
            'fechaFinalizacion': instance.fechaFinalizacion,
            
            'estadoProducto': instance.estadoProducto,
            'idProducto': [
                instance.idProducto.nombre,
                instance.idProducto.descripcion,
                instance.idProducto.valor,
                instance.idProducto.imagen,
            ]
        }