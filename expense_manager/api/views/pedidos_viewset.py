from expense_manager.api.serializers.pedido_serializer import *
from expense_manager.models import *

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


#* List of API PedidosPendientes
class PedidosPendientesViewSet(viewsets.ModelViewSet):
    serializer_class = ListPedidosPendientesSerializers
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['idProducto__nombre', 'idPersona__username', 'idProducto__idProducto', 'idComprobante__nombre', 'fechaPedido', 'estadoPedido']
    search_fields = ['idProducto__nombre', 'idPersona__username', ' estadoPedido']
    ordering_fields = ['idPedidosPendientes', 'idPersona', 'idProducto']


    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idPedidosPendientes=pk, estadoCreacion=True).first()

    def create(self, request):
        serializer = PedidosPendientesSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'PedidoPendiente creado correctamente!'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'No se pudo crear el PedidoPendiente!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            pedidoPendiente_serializer = PedidosPendientesSerializers(self.get_queryset(pk), data=request.data)

            if pedidoPendiente_serializer.is_valid():
                pedidoPendiente_serializer.save()
                return Response({'message': 'Pedido Pendiente actualizado correctamente!'}, status=status.HTTP_200_OK)

            return Response({'message': 'No se pudo actualizar los datos del Pedido Pendiente!!', 'error': pedidoPendiente_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pedidopendiente = self.get_queryset().filter(
            idPedidosPendientes=pk).first()  # get instance
        if pedidopendiente:
            pedidopendiente.estadoCreacion = False
            pedidopendiente.save()
            return Response({'message': 'Pedido Pendiente eliminado correctamente!'}, status=status.HTTP_200_OK)

        return Response({'error': 'No existe un Pedido Pendiente con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
