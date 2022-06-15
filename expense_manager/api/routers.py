from rest_framework.routers import DefaultRouter
from expense_manager.api.views.general_viewset import *
from expense_manager.api.views.pedidos_viewset import *
from expense_manager.api.views.detalle_viewset import *

router = DefaultRouter()

router.register(r'pedido', PedidosPendientesViewSet, basename = 'pedidos-pendientes')
router.register(r'detalleCompra', DetalleCompraViewSet, basename = 'detalles-Compra')
router.register(r'tipoPago', TipoPagoViewSet, basename = 'tipo-pago')
router.register(r'comprobantePago', ComprobantePagoViewSet, basename = 'comprobante-pago')

urlpatterns = router.urls