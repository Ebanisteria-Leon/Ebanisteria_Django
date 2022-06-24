from datetime import date
from products.models import Producto, Promocion
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apscheduler.schedulers.background import BackgroundScheduler

from products.api.serializer.promo_serializers import *

scheduler = BackgroundScheduler()

#* Create and List for promocion API
class PromocionViewSet(viewsets.ModelViewSet):
    serializer_class = ListPromocionSerializers

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['productoExtra',
                        'valorDescuento', 'idProducto__nombre']
    search_fields = ['productoExtra', 'valorDescuento', 'idProducto__nombre']
    ordering_fields = ['idPromociones__nombre']
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True)

        return self.get_serializer().Meta.model.objects.filter(idPromociones = pk, estadoCreacion = True).first()
    
    def create(self, request):
        serializer = PromocionSerializers(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Promocion creada correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        if self.get_queryset(pk):
            promocion_serializer = PromocionSerializers(self.get_queryset(pk), data = request.data)
            
            if promocion_serializer.is_valid():
                promocion_serializer.save()
                return Response({'data': promocion_serializer.data, 'message': 'Promocion actualizada correctamente'}, status = status.HTTP_200_OK)
            
            return Response(promocion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk = None):
        promocion = self.get_queryset().filter(idPromociones = pk).first()
        
        if promocion:
            promocion.estadoCreacion = False
            promocion.save()
            return Response({'message': 'Promocion eliminada correctamente'}, status = status.HTTP_200_OK)
        
        return Response({'error': 'No existe una Promocion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

    @scheduler.scheduled_job('interval', seconds=60)
    def validacion_destacado_fecha_promocion():
        promocion_detalle = Promocion.objects.filter()
        for de_promocion in promocion_detalle:
            
            if de_promocion.fechaFinalizacion == None:
                pass

            else:
                if de_promocion.fecha_limite_promocion == True and de_promocion.tiempoPromocion:
                    de_promocion.tiempoPromocion = 'NP'
                    de_promocion.save()
                else:
                    pass

    scheduler.start()
