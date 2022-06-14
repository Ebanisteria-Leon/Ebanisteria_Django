from django.db import models
from users.models import *
from base.models import *

# Create your models here.

#* Tabla de Categorias
class Categoria(BaseModel):
    idCategoria = models.AutoField(primary_key = True, verbose_name = 'Identificador de Categoria')
    nombreCategoria = models.CharField(max_length = 200, verbose_name = 'Nombre Categoria')
    descripcion = models.TextField(verbose_name = 'Descripcion', null = True, blank = True)

    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        return self.nombreCategoria

#* Tabla de productos
class Producto(BaseModel):
    idProducto = models.AutoField(primary_key = True, verbose_name = 'Identificador del Producto')
    nombre = models.CharField(max_length = 30, verbose_name = 'Nombre Producto')

    descripcion = models.TextField(verbose_name = 'Descripcion', null = True, blank = True)
    valor = models.FloatField(verbose_name = 'Valor del Producto')
    alto = models.CharField(max_length = 50, verbose_name = 'Medidas del Producto(Altura)')
    largo = models.CharField(max_length = 50, verbose_name = 'Medidas del Producto(Largo)')
    ancho = models.CharField(max_length = 50, verbose_name = 'Medidas del Producto(Anchura)')
    color = models.CharField(max_length = 255, null = True, blank = True)
    calificacion = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Calificacion de productos')
    
    imagen = models.TextField(verbose_name = 'Nombre producto Imagenes', null = True, blank = True)
    imagen2 = models.TextField(verbose_name = 'Nombre producto Imagenes 2', null = True, blank = True)

    fechaInicio = models.DateField(verbose_name = 'Fecha de Inicio')
    fechaFinalizacion = models.DateField(verbose_name = 'Fecha de Finalizacion')

    estadoProducto = models.CharField(verbose_name = 'Estado del Producto', max_length = 30, default = '')
    destacado = models.CharField(verbose_name = 'Tipo del Producto', max_length = 30, default = '')
    tiempoProducto = models.CharField(verbose_name = 'Tiempo del Producto', max_length = 30, default = '')

    idCategoria = models.ForeignKey(Categoria, on_delete = models.CASCADE,verbose_name = 'Indicador de Categoria')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre

#* Tabla de Promociones
class Promocion(BaseModel):
    idPromociones = models.AutoField(primary_key = True, null = False, verbose_name = 'Identificador de Promociones')
    nombre = models.CharField(max_length = 30, verbose_name = 'Nombre de la Promocion')
    
    valorDescuento = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Valor del Descuento del Producto')
    productoExtra = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Cantidad de Productos extra')
    
    fechaInicio = models.DateField(verbose_name = 'Fecha de Inicio', null = True)
    fechaFinalizacion = models.DateField(verbose_name = 'Fecha de Finalizacion', null = True)
    
    estadoPromocion = models.CharField(max_length = 30, default = '', verbose_name = 'Estado de la Promocion')
    tiempoPromocion = models.CharField(max_length = 30, default = '', verbose_name = 'Tiempo de la Promocion')
    
    idProducto = models.ForeignKey(Producto, default = '', on_delete=models.CASCADE, verbose_name='Identificar del Producto')

    class Meta:
        verbose_name = 'Promocion de Producto'
        verbose_name_plural = 'Promociones de Productos'

    def __str__(self):
        return f'Oferta del producto : {self.nombre}'