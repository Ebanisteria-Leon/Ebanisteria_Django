from products.models import *
from products.api.serializer.image_serializers import *

from base.utils import validate_files

from rest_framework import status, viewsets
from rest_framework.response import Response

#* Create and List of API Imagen
class ImagenViewSet(viewsets.ModelViewSet):
    serializer_class = ImagenesProductoSerializers
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(idImagen = self.kwargs['pk'], estadoCreacion=True)
    
    def list(self, request):
        imagen_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response (imagen_serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        data = validate_files(request.data, 'imagenProducto')
        serializer = self.serializer_class(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Imagen creada correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response({'message': '','error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        if self.get_object().exists():
            data = validate_files(request.data, 'imagenProducto', True)
            serializer = self.serialzer_class(instance = self.get_object().get(), data = data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Imagen Actualizada Correctamente!'}, status = status.HTTP_200_OK)
            
        return Response({'message': '', 'error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk = None):
        if self.get_object().exists():
            self.get_object().get().estadoCreacion = False
            return Response({'message':'Categoría eliminada correctamente!'}, status = status.HTTP_200_OK)
        
        return Response({'message':'', 'error':'No existe una Imagen con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)