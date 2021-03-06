from products.models import *
from products.api.serializer.category_serializers import *

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

#* Create and List of API Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    filterset_fields = ['nombreCategoria']
    search_fields = ['nombreCategoria']
    
    serializer_class = CategoriaSerializers
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True)

        return self.get_serializer().Meta.model.objects.filter(idCategoria = pk, estadoCreacion = True).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Categoria creada correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        if self.get_queryset(pk):
            categoria_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if categoria_serializer.is_valid():
                categoria_serializer.save()
                return Response({'message': 'Categoria Actualizada Correctamente!'}, status = status.HTTP_200_OK)
            
        return Response({'message': 'No se puedo Actualizar la Categoria!', 'error': categoria_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk = None):
        categoria = self.get_queryset().filter(idCategoria = pk).first()
        
        if categoria:
            categoria.estadoCreacion = False
            categoria.save()
            return Response({'message':'Categoría eliminada correctamente!'}, status = status.HTTP_200_OK)
        
        return Response({'message':'No se puedo Eliminar la Categoria!', 'error':'No existe una Categoria con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)