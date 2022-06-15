from expense_manager.models import *
from expense_manager.api.serializers.general_serializer import *

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

#* List of API Comprobante pago
class ComprobantePagoViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['nombre']
    search_fields = ['nombre']
    
    serializer_class = ComprobantePagoSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idcomprobantePago=pk, estadoCreacion=True).first()

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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['nombre']
    search_fields = ['nombre']
    
    serializer_class = TipoPagoSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estadoCreacion=True)

        return self.get_serializer().Meta.model.objects.filter(idTipoPago=pk, estadoCreacion=True).first()

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
