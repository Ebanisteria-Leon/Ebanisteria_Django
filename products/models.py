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

opciones_estados = [
    [0, 'Nuevo'],
    [1, 'Cancelado'],
    [2, 'Pendiente'],
    [3, 'Enviado'],
    [4, 'Produccion'],
    [5, 'Destacado'],
]

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
    
    imagen = models.CharField(verbose_name = 'Nombre producto Imagenes', null = True, blank = True, max_length = 255)
    imagen2 = models.TextField(verbose_name = 'Nombre producto Imagenes 2', null = True, blank = True)

    # destacados = models.BooleanField(verbose_name = 'Productos destacados', default = True)

    fechaInicio = models.DateField(verbose_name = 'Fecha de Inicio')
    fechaFinalizacion = models.DateField(verbose_name = 'Fecha de Finalizacion')

    estadoProducto = models.IntegerField(verbose_name = 'Estado del Producto', choices = opciones_estados, default = 0)
    idCategoria = models.ForeignKey(Categoria, on_delete = models.CASCADE,verbose_name = 'Indicador de Categoria')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
    
    @property
    def stock(self):
        from django.db.models import Sum
        from expense_manager.models import DetallesCompra
        
        expenses = DetallesCompra.objects.filter(
            idProductos = self,
            estadoCreacion = True
        ).aggregate(Sum('cantidad'))
        
        return expenses

#* Tabla de Promociones
class Promocion(BaseModel):
    idPromociones = models.AutoField(primary_key = True, null = False, verbose_name = 'Identificador de Promociones')
    nombre = models.CharField(max_length = 30, verbose_name = 'Nombre de la Promocion')
    valorDescuento = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Valor del Descuento del Producto')
    productoExtra = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Cantidad de Productos extra')
    idProducto = models.ManyToManyField(Producto, verbose_name = 'Identificar del Producto')

    class Meta:
        verbose_name = 'Promocion de Producto'
        verbose_name_plural = 'Promociones de Productos'

    def __str__(self):
        return f'Oferta del producto : {self.nombre}'