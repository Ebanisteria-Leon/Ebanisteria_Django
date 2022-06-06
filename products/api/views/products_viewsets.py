from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from products.api.serializer.product_serializers import *

# from base.utils import validate_files

#* Create and List for productos API
class ProductoViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['estadoProducto', 'destacado', 'tiempoProducto', 'fechaInicio', 'fechaFinalizacion', 'calificacion', 'idCategoria__nombreCategoria']
    search_fields = ['estadoProducto', 'destacado', 'tiempoProducto', 'calificacion', 'idCategoria__nombreCategoria']
    ordering_fields = ['idProducto__calificacion', 'idProducto__valor', 'idProducto__idProducto']
    
    serializer_class = ProductoSerializers

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True)
        
        return self.get_serializer().Meta.model.objects.filter(idProducto = pk, estadoCreacion = True).first()

    def list(self, request):
        producto_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(producto_serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response({'message': 'No se pudo crear el Producto!', 'error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        producto = self.get_queryset(pk)
        
        if producto:
            producto_serializer = ProductoRetrieveSerializer(producto)
            return Response(producto_serializer.data, status = status.HTTP_200_OK)
        
        return Response({'error': 'No existe un producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if producto_serializer.is_valid():
                producto_serializer.save()
                return Response({'message': 'Producto actualizado correctamente!'}, status = status.HTTP_200_OK)
            
            return Response({'message': 'No se pudo actualizar los datos del Producto!!', 'error': producto_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        producto = self.get_queryset().filter(idProducto = pk).first()  # get instance
        if producto:
            producto.estadoCreacion = False
            producto.save()
            return Response({'message': 'Producto eliminado correctamente!'}, status = status.HTTP_200_OK)
        
        return Response({'error': 'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)