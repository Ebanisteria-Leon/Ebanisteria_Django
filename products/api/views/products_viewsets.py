from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apscheduler.schedulers.background import BackgroundScheduler

from products.api.serializer.product_serializers import *

scheduler = BackgroundScheduler()

#* View Productos API
class ProductoViewSet(viewsets.ModelViewSet):

    serializer_class = ProductoSerializers

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['nombre', 'estadoProducto', 'destacado', 'tiempoProducto', 'fechaInicio', 'fechaFinalizacion', 'calificacion', 'idCategoria__nombreCategoria']

    search_fields = ['nombre', 'estadoProducto', 'destacado', 'tiempoProducto', 'calificacion', 'idCategoria__nombreCategoria']

    ordering_fields = ['calificacion', 'valor', 'idProducto']

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idProducto=pk, estadoCreacion=True).first()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'No se pudo crear el Producto!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)

            if producto_serializer.is_valid():
                producto_serializer.save()
                return Response({'message': 'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)

            return Response({'message': 'No se pudo actualizar los datos del Producto!!', 'error': producto_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        producto = self.get_queryset().filter(idProducto=pk).first()  # get instance
        if producto:
            producto.estadoCreacion = False
            producto.save()
            return Response({'message': 'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)

        return Response({'error': 'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    @scheduler.scheduled_job('interval', day = 1)
    def validacion_destacado_fecha_producto():
        producto_detalle = Producto.objects.filter()
        for de_producto in producto_detalle:

            if de_producto.fechaFinalizacion == None:
                pass

            else:
                if de_producto.fecha_limite_producto == True and de_producto.tiempoProducto == 'NUE':
                    de_producto.tiempoProducto = 'ANT'
                    de_producto.save()
                else:
                    pass

    scheduler.start()
