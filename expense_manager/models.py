from django.db import models

from base.models import BaseModel
from users.models import User
from products.models import *

# Create your models here.

#* Tabla de Tipo de pago
class TipoPago(BaseModel):
    idTipoPago = models.AutoField(primary_key = True, verbose_name = 'Identificador de Tipo de Pago')
    nombre = models.CharField('Nombre de Medio de Pago', max_length = 100)

    class Meta:
        ordering = ['idTipoPago']
        verbose_name = 'Medio de Pago'
        verbose_name_plural = 'Medio de Pagos'

    def __str__(self):
        return self.name

class ComprobantePago(BaseModel):
    idComprobantePago = models.AutoField(primary_key = True, verbose_name = 'Identificador de Comprobante de Pago')
    nombre = models.CharField('Nombre de comprobante de Pago', max_length = 100)

    class Meta:
        ordering = ['idComprobantePago']
        verbose_name = 'Comprobante'
        verbose_name_plural = 'Comprobantes'

    def __str__(self):
        return self.name

#* Tabla de detalles compra
class DetallesCompra(BaseModel):
    idDetallesCompra = models.AutoField(primary_key = True, null = False, verbose_name = 'Indicador de Compra')
    cantidad = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Cantidad Productos')

    vUnitario = models.FloatField(verbose_name = 'Valor Unitario')
    vTotal = models.FloatField(verbose_name = 'Valor Total')

    fechaCompra = models.DateField(verbose_name = 'Fecha Compra', auto_now = False, auto_now_add = False)

    estadoCompra = models.CharField(max_length = 30, verbose_name = 'Estado de la Compra', default = '')
    comprobante_number = models.CharField(max_length = 50, verbose_name = 'Numero de comprobante', default = '')

    idComprobante = models.ForeignKey(ComprobantePago, on_delete = models.CASCADE, verbose_name = 'Identificador de Comprobante de Pago')
    idTipoPago = models.ForeignKey(TipoPago, on_delete = models.CASCADE, verbose_name = 'Identificador de tipo de Pago')
    idProductos = models.ManyToManyField(Producto, verbose_name = 'Indicador del Producto')
    idPersona = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Indicador de la Persona')

    class Meta:
        verbose_name = 'Detalles de la compra'

    def __str__(self):
        return f'Detalles de la compra en la fecha : {self.fechaCompra}'

#* Tabla de pedidosPendientes
class PedidosPendiente(BaseModel):
    idPedidosPendientes = models.AutoField(primary_key = True, verbose_name = 'Identificador de los Pedidos')
    fechaPedido = models.DateField(verbose_name = 'Fecha del Pedido')
    estadoPedido = models.CharField(max_length = 30, verbose_name = 'Estado del Pedido', default = '')

    idComprobante = models.ForeignKey(ComprobantePago, on_delete = models.CASCADE, verbose_name='Identificador de Comprobante de Pago')
    idTipoPago = models.ForeignKey(TipoPago, on_delete = models.CASCADE, verbose_name = 'Identificador de tipo de Pago')
    idProducto = models.ManyToManyField(Producto, verbose_name = 'Identificador del Producto')
    idPersona = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Identificador de la Persona')

    class Meta:
        verbose_name = 'Pedido pendiente'
        verbose_name_plural = 'Pedidos pendientes'
