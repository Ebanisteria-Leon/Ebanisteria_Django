from rest_framework import status, viewsets
from rest_framework.response import Response

from products.api.serializer.promo_serializers import PromocionSerializers

class PromocionViewSet(viewsets.ModelViewSet):
    serializer_class = PromocionSerializers
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True, idProducto = pk).first()
    
    def list(self, request):
        promocion_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response (promocion_serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Promocion creada correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        if self.get_queryset(pk):
            promocion_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if promocion_serializer.is_valid():
                promocion_serializer.save()
                return Response(promocion_serializer.data, status = status.HTTP_200_OK)
            
            return Response(promocion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk = None):
        promocion = self.get_queryset().filter(idPromocion = pk).first()
        
        if promocion:
            promocion.state = False
            promocion.save()
            return Response({'message': 'Promocion eliminada correctamente'}, status = status.HTTP_200_OK)
        
        return Response({'error': 'No existe una Promocion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
