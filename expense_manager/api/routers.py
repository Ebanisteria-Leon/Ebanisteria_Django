from rest_framework.routers import DefaultRouter
from expense_manager.api.general_viewset import *

router = DefaultRouter()

router.register(r'pedido', PedidosPendientesViewSet, basename = 'pedidos-Pendientes')
router.register(r'detalleCompra', DetalleCompraViewSet, basename = 'detalles-Compra')

urlpatterns = router.urls