from products.models import Promocion

from rest_framework import serializers

class PromocionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        exclude = ('estadoCreacion', 'fechaCreacion', 'fechaModificacion', 'fechaEliminacion')
    
    def validate_product(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Debe ingresar un Producto')
        
        return value
    
    def validate(self, data):
        if 'idProducto' not in data.keys():
            raise serializers.ValidationError({
                    'idProducto': 'Debe ingresar un Producto'
                })
        
        return data
    
    def to_representation(self, instance):
        return {
            'idPromocion': instance.idPromocion,
            'nombre': instance.nombre,
            
            'valorDescuento': instance.valorDescuento,
            'productoExtra': instance.productoExtra,
            
            'estadoProducto': instance.estadoProducto,
            'idProducto': [
                instance.idProducto.nombre,
                instance.idProducto.descripcion,
                instance.idProducto.valor,
            ]
        }