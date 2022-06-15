from expense_manager.api.serializers.pedido_serializer import *
from expense_manager.models import *

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


#* List of API PedidosPendientes
class PedidosPendientesViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['idProducto__nombre', 'idPersona__username', 'idComprobante__nombre', 'fechaPedido', 'estadoPedido']
    search_fields = ['idProducto__nombre', 'idPersona__username', ' estadoPedido']

    serializer_class = ListPedidosPendientesSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idPedidoPendiente=pk, estadoCreacion=True).first()

    def create(self, request):
        serializer = PedidosPendientesSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'PedidoPendiente creado correctamente!'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'No se pudo crear el PedidoPendiente!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            pedidopendiente_serializer = PedidosPendientesSerializers(
                self.get_queryset(pk), data=request.data)

            if pedidopendiente_serializer.is_valid():
                pedidopendiente_serializer.save()
                return Response({'message': 'PedidoPendiente actualizado correctamente!'}, status=status.HTTP_200_OK)

            return Response({'message': 'No se pudo actualizar los datos del PedidoPendiente!!', 'error': pedidopendiente_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pedidopendiente = self.get_queryset().filter(
            idPedidoPendiente=pk).first()  # get instance
        if pedidopendiente:
            pedidopendiente.estadoCreacion = False
            pedidopendiente.save()
            return Response({'message': 'PedidoPendiente eliminado correctamente!'}, status=status.HTTP_200_OK)

        return Response({'error': 'No existe un PedidoPendiente con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
