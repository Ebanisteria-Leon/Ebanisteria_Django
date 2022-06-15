from expense_manager.models import *
from expense_manager.api.serializers.detalle_serializer import *

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

#* List of API DetallesCompra
class DetalleCompraViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['idProductos__nombre', 'idPersona__username', 'idProducto__idProducto', 'idComprobante__nombre', 'cantidad', 'estadoCompra']
    search_fields = ['idProductos__nombre', 'idPersona__username',' estadoCompra']
    
    serializer_class = ListDetallesCompraSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idDetalleCompra=pk, estadoCreacion=True).first()

    def create(self, request):
        serializer = DetallesCompraSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'DetalleCompra creado correctamente!'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'No se pudo crear el DetalleCompra!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            detallecompra_serializer = DetallesCompraSerializers(
                self.get_queryset(pk), data=request.data)

            if detallecompra_serializer.is_valid():
                detallecompra_serializer.save()
                return Response({'message': 'DetalleCompra actualizado correctamente!'}, status=status.HTTP_200_OK)

            return Response({'message': 'No se pudo actualizar los datos del DetalleCompra!!', 'error': detallecompra_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        detallecompra = self.get_queryset().filter(idDetalleCompra=pk).first()  # get instance
        if detallecompra:
            detallecompra.estadoCreacion = False
            detallecompra.save()
            return Response({'message': 'DetalleCompra eliminado correctamente!'}, status=status.HTTP_200_OK)

        return Response({'error': 'No existe un DetalleCompra con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
