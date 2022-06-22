from datetime import date
from products.models import Producto, Promocion
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apscheduler.schedulers.background import BackgroundScheduler

from products.api.serializer.promo_serializers import PromocionSerializers

scheduler = BackgroundScheduler()

#* Create and List for promocion API
class PromocionViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['productoExtra', 'valorDescuento', 'idProducto__nombre']
    search_fields = ['productoExtra', 'valorDescuento', 'idProducto__nombre']
    ordering_fields = ['idPromocion__nombre']
    
    serializer_class = PromocionSerializers
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True)

        return self.get_serializer().Meta.model.objects.filter(idPromocion = pk, estadoCreacion = True).first()
    
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
            # productos = request.data.get('productos')
            
            if promocion_serializer.is_valid():
                # estadoPromo= request.data.get('estadoPromocion')
                
                """if estadoPromo == 'AC':
                    promocion_serializer.save()
                    return Response({'data': promocion_serializer.data, 'message': 'Promocion actualizada correctamente'}, status = status.HTTP_200_OK)
                
                elif estadoPromo == 'IC':
                    #* Creacion de la Promocion
                    error_producto = {}
                    productos_promocion = {}
                    
                    #* Creacion detalles promocion
                    producto = Producto.objects.filter(idProducto = request.data.get('idPromocion')).first()
                    promocion = Promocion(idPromocion = producto, fechaInico = date.today(), estadoPromo = 'AC')
                    
                    #* Creacion de Promociones
                    for idProducto in productos:
                        if producto.estadoProducto == 'NP':
                            producto.estadoProducto == 'PRO'
                            productos_promocion['Promocion ' + str(idProducto)] = producto
                        
                        else:
                            error_producto['producto ' + str(idProducto)] = 'No se encuentra en promocion'"""
            
            return Response(promocion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk = None):
        promocion = self.get_queryset().filter(idPromocion = pk).first()
        
        if promocion:
            promocion.state = False
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
