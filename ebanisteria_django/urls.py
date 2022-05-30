from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from payments.views import ProcessWebhookView

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api.views import *

schema_view = get_schema_view(
    openapi.Info(
        title = 'Dcoumentacion de API Ebanisteria Leon',
        default_version = 'v1',
        description = 'Documentacion Publica de API Ebanisteria Leon 2022',
        terms_of_service = 'https://www.google.com/policies/terms/',
        contact = openapi.Contact(email = 'gojan.1407holguin@gmail.com'),
        license = openapi.License(name = 'BSD License'),
    ),
    public = True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    #* Documentacion del backend 
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout = 0), name = 'schema-json'),
    re_path('^swagger/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema-swagger-ui'),
    re_path('^redoc/', schema_view.with_ui('redoc', cache_timeout = 0), name = 'schema-redoc'),

    path('admin/', admin.site.urls),
    
    path('users/', include('users.api.routers')), #*API Root para el aplicacion de usuarios
    path('api/', include('products.api.routers')), #*API Root para el aplicacion de productos
    path('detail/', include('expense_manager.api.routers')), #*API Root para el aplicacion de facturacion
    path('webhooks/paypal/', ProcessWebhookView.as_view(), name = 'webhook_paypal'),
    
    #* Generacion de tokens
    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    
    #* Login, Logut para usuarios
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    
    #path('api-auth/', include('rest_framework.urls')),
    
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]