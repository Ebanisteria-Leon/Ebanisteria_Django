from django.contrib import admin
from products.models import *

# List the registration of your models
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('idCategoria', 'nombreCategoria')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('idProducto', 'nombre')

class PromocionAdmin(admin.ModelAdmin):
    list_display = ('idPromociones', 'nombre')

"""class ImagenesProductosAdmin(admin.ModelAdmin):
    list_display = ('idImagenes', 'nombreProducto')"""

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Promocion, PromocionAdmin)
#admin.site.register(ImagenesProductos, ImagenesProductosAdmin)
