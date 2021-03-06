from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import User
from users.api.serializers import *

class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializers
    list_serializer_class = UserListSerializers
    queryset = None
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['username', 'email', 'rolUser']

    ordering_fields = ['id']
    
    def get_object(self, pk):
        return get_object_or_404(self.model, pk = pk)
    
    #* Queryset
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(is_active = True)
        
        return self.queryset
    
    @action(detail = True, methods = ['post'])
    def set_password(self, request, pk = None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializers(data = request.data)
        
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': 'Contraseña actualizada correctamente!'
            })
            
        return Response({
            'message': 'Hay errores en la información enviada!',
            'errors': password_serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)
    
    #* GET ALL USERS
    
    #* List
    def list(self, request):
        users = self.get_queryset()
        users_serialzer = self.list_serializer_class(users, many = True)
        return Response(users_serialzer.data, status = status.HTTP_200_OK)
    
    #* POST USERS
    
    #* Create
    def create(self, request):
        user_serializer = self.serializer_class(data = request.data)
        
        #* Validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                    'message': 'Usuario Registrado Correctamente!'
                }, status = status.HTTP_201_CREATED)
            
        return Response({
                'message': 'Hay errores en el registro!',
                'errors': user_serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)
    
    #* Retrive
    def retrieve(self, request, pk = None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data, status = status.HTTP_200_OK)
    
    #* Update
    def update(self, request, pk = None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializers(user, data = request.data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                    'message': 'Usuario actualizado correctamente!'
                }, status = status.HTTP_200_OK)
            
        return Response({
            'message': 'Hay errores al querer actualizar!',
            'errors': user_serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)
    
    #* Delete
    def destroy(self, request, pk = None):
        user_destroy = self.model.objects.filter(id = pk).update(is_active = False)
        
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente!'
            }, status = status.HTTP_204_NO_CONTENT)
            
        return Response({
                'message': 'No existe el usuario que desea eliminar!'
            }, status = status.HTTP_404_NOT_FOUND)