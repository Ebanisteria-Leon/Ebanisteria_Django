from expense_manager.models import *
from expense_manager.api.general_serializer import *

from rest_framework import viewsets, status
from rest_framework.response import Response

#* List of API DetallesCompra
class DetalleCompraViewSet(viewsets.ModelViewSet):
    serializer_class = DetallesCompraSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idDetalleCompra=pk, estadoCreacion=True).first()

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'DetalleCompra creado correctamente!'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'No se pudo crear el DetalleCompra!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            detallecompra_serializer = self.serializer_class(
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

#* List of API PedidosPendientes
class PedidosPendientesViewSet(viewsets.ModelViewSet):
    serializer_class = PedidosPendientesSerializers

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion = True)
        
        return self.get_serializer().Meta.model.objects.filter(idPedidoPendiente = pk, estadoCreacion = True).first()

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'PedidoPendiente creado correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response({'message': 'No se pudo crear el PedidoPendiente!', 'error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        if self.get_queryset(pk):
            pedidopendiente_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if pedidopendiente_serializer.is_valid():
                pedidopendiente_serializer.save()
                return Response({'message': 'PedidoPendiente actualizado correctamente!'}, status = status.HTTP_200_OK)
            
            return Response({'message': 'No se pudo actualizar los datos del PedidoPendiente!!', 'error': pedidopendiente_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        pedidopendiente = self.get_queryset().filter(idPedidoPendiente = pk).first()  # get instance
        if pedidopendiente:
            pedidopendiente.estadoCreacion = False
            pedidopendiente.save()
            return Response({'message': 'PedidoPendiente eliminado correctamente!'}, status = status.HTTP_200_OK)
        
        return Response({'error': 'No existe un PedidoPendiente con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#* List of API Comprobante pago
class ComprobantePagoViewSet(viewsets.ModelViewSet):
    serializer_class = ComprobantePagoSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idcomprobantePago=pk, estadoCreacion=True).first()

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'comprobantePago creado correctamente!'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'No se pudo crear el comprobantePago!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            comprobantePago_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)

            if comprobantePago_serializer.is_valid():
                comprobantePago_serializer.save()
                return Response({'message': 'comprobantePago actualizado correctamente!'}, status=status.HTTP_200_OK)

            return Response({'message': 'No se pudo actualizar los datos del comprobantePago!!', 'error': comprobantePago_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        comprobantePago = self.get_queryset().filter(
            idComprobantePago=pk).first()  # get instance
        if comprobantePago:
            comprobantePago.estadoCreacion = False
            comprobantePago.save()
            return Response({'message': 'comprobantePago eliminado correctamente!'}, status=status.HTTP_200_OK)

        return Response({'error': 'No existe un comprobantePago con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

#* List of API TipoPago
class TipoPagoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoPagoSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idTipoPago=pk, estadoCreacion=True).first()

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'TipoPago creado correctamente!'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'No se pudo crear eTipoPago!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            tipoPago_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)

            if tipoPago_serializer.is_valid():
                tipoPago_serializer.save()
                return Response({'message':'TipoPago actualizado correctamente!'}, status=status.HTTP_200_OK)

            return Response({'message': 'No se pudo actualizar los datos deTipoPago!!', 'error':tipoPago_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        tipoPago = self.get_queryset().filter(
            TipoPago=pk).first()  # get instance
        if tipoPago:
            TipoPago.estadoCreacion = False
            TipoPago.save()
            return Response({'message':'TipoPago eliminado correctamente!'}, status=status.HTTP_200_OK)

        return Response({'error': 'No existe un TipoPago con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
