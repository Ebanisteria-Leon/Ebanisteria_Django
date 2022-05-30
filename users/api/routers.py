from rest_framework.routers import DefaultRouter

from users.api.api import UserViewSet

router = DefaultRouter()

router.register(r'usuario', UserViewSet, basename='usuarios')

urlpatterns = router.urls
