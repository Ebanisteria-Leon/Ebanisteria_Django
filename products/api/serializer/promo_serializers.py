from products.models import Promocion

from rest_framework import serializers

class PromocionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
    
    def to_representation(self, instance):
        return {
            'idPromociones': instance.idPromociones,
            'nombre': instance.nombre,
            
            'valorDescuento': instance.valorDescuento,
            'productoExtra': instance.productoExtra,
            
            'fechaInicio': instance.fechaInicio,
            'fechaFinalizacion': instance.fechaFinalizacion,
            
            'estadoPromocion': instance.estadoPromocion,
            'tiempoPromocion': instance.tiempoPromocion,
            
            'idProducto': [
                instance.idProducto.nombre,
                instance.idProducto.descripcion,
                instance.idProducto.valor,
                instance.idProducto.imagen,
            ]
        }