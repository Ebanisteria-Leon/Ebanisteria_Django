from products.models import *
from products.api.serializer.category_serializers import *

from rest_framework import status, viewsets
from rest_framework.response import Response

#* Create and List of API Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializers
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(idCategoria = self.kwargs['pk'], estadoCreacion=True)
    
    def list(self, request):
        categoria_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response (categoria_serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Categoria creada correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        if self.get_object().exists():
            serializer = self.serialzer_class(instance = self.get_object().get(), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Categoria Actualizada Correctamente!'}, status = status.HTTP_200_OK)
            
        return Response({'message': '', 'error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk = None):
        if self.get_object().exists():
            self.get_object().get().estadoCreacion = False
            return Response({'message':'Categoría eliminada correctamente!'}, status = status.HTTP_200_OK)
        
        return Response({'message':'', 'error':'No existe una Categoria con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)