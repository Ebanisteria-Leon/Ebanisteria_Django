from rest_framework.routers import DefaultRouter

from products.api.views.products_viewsets import ProductoViewSet
from products.api.views.promo_viewsets import PromocionViewSet
from products.api.views.category_viewsets import CategoriaViewSet
from products.api.views.image_viewsets import ImagenViewSet

router = DefaultRouter()

router.register(r'producto', ProductoViewSet, basename = 'productos')
router.register(r'promocion', PromocionViewSet, basename = 'promociones')
router.register(r'categoria', CategoriaViewSet, basename = 'categorias')
router.register(r'imagen', ImagenViewSet, basename = 'imagenes')

urlpatterns = router.urls
