from expense_manager.models import *
from expense_manager.api.general_serializer import *

from rest_framework import viewsets
from rest_framework.response import Response

#* List of API DetallesCompra
class DetalleCompraViewSet(viewsets.ModelViewSet):
    serializer_class = DetallesCompraSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

#* List of API PedidosPendientes
class PedidosPendientesViewSet(viewsets.ModelViewSet):
    serializer_class = PedidosPendientesSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)