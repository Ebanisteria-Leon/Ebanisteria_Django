# Generated by Django 3.2.9 on 2022-06-22 21:05

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobantePago',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('idComprobantePago', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de Comprobante de Pago')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de comprobante de Pago')),
            ],
            options={
                'verbose_name': 'Comprobante',
                'verbose_name_plural': 'Comprobantes',
                'ordering': ['idComprobantePago'],
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('idTipoPago', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de Tipo de Pago')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Medio de Pago')),
            ],
            options={
                'verbose_name': 'Medio de Pago',
                'verbose_name_plural': 'Medio de Pagos',
                'ordering': ['idTipoPago'],
            },
        ),
        migrations.CreateModel(
            name='PedidosPendiente',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('idPedidosPendientes', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de los Pedidos')),
                ('fechaPedido', models.DateField(verbose_name='Fecha del Pedido')),
                ('estadoPedido', models.CharField(default='', max_length=30, verbose_name='Estado del Pedido')),
                ('idComprobante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense_manager.comprobantepago', verbose_name='Identificador de Comprobante de Pago')),
                ('idPersona', models.ManyToManyField(to='users.User', verbose_name='Identificador de la Persona')),
                ('idProducto', models.ManyToManyField(to='products.Producto', verbose_name='Identificador del Producto')),
                ('idTipoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense_manager.tipopago', verbose_name='Identificador de tipo de Pago')),
            ],
            options={
                'verbose_name': 'Pedido pendiente',
                'verbose_name_plural': 'Pedidos pendientes',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTipoPago',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('idTipoPago', models.IntegerField(blank=True, db_index=True, verbose_name='Identificador de Tipo de Pago')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Medio de Pago')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.user')),
            ],
            options={
                'verbose_name': 'historical Medio de Pago',
                'verbose_name_plural': 'historical Medio de Pagos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPedidosPendiente',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('idPedidosPendientes', models.IntegerField(blank=True, db_index=True, verbose_name='Identificador de los Pedidos')),
                ('fechaPedido', models.DateField(verbose_name='Fecha del Pedido')),
                ('estadoPedido', models.CharField(default='', max_length=30, verbose_name='Estado del Pedido')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.user')),
                ('idComprobante', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='expense_manager.comprobantepago', verbose_name='Identificador de Comprobante de Pago')),
                ('idTipoPago', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='expense_manager.tipopago', verbose_name='Identificador de tipo de Pago')),
            ],
            options={
                'verbose_name': 'historical Pedido pendiente',
                'verbose_name_plural': 'historical Pedidos pendientes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDetallesCompra',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('idDetallesCompra', models.IntegerField(blank=True, db_index=True, verbose_name='Indicador de Compra')),
                ('cantidad', models.PositiveSmallIntegerField(default=0, verbose_name='Cantidad Productos')),
                ('vUnitario', models.FloatField(verbose_name='Valor Unitario')),
                ('vTotal', models.FloatField(verbose_name='Valor Total')),
                ('fechaCompra', models.DateField(verbose_name='Fecha Compra')),
                ('estadoCompra', models.CharField(default='', max_length=30, verbose_name='Estado de la Compra')),
                ('comprobante_number', models.CharField(default='', max_length=50, verbose_name='Numero de comprobante')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.user')),
                ('idComprobante', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='expense_manager.comprobantepago', verbose_name='Identificador de Comprobante de Pago')),
                ('idPersona', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='users.user', verbose_name='Indicador de la Persona')),
                ('idTipoPago', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='expense_manager.tipopago', verbose_name='Identificador de tipo de Pago')),
            ],
            options={
                'verbose_name': 'historical Detalles de la compra',
                'verbose_name_plural': 'historical Detalles de la compras',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalComprobantePago',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('idComprobantePago', models.IntegerField(blank=True, db_index=True, verbose_name='Identificador de Comprobante de Pago')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de comprobante de Pago')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.user')),
            ],
            options={
                'verbose_name': 'historical Comprobante',
                'verbose_name_plural': 'historical Comprobantes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='DetallesCompra',
            fields=[
                ('estadoCreacion', models.BooleanField(default=True, verbose_name='Estado de Creacion')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Modificacion')),
                ('fechaEliminacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('idDetallesCompra', models.AutoField(primary_key=True, serialize=False, verbose_name='Indicador de Compra')),
                ('cantidad', models.PositiveSmallIntegerField(default=0, verbose_name='Cantidad Productos')),
                ('vUnitario', models.FloatField(verbose_name='Valor Unitario')),
                ('vTotal', models.FloatField(verbose_name='Valor Total')),
                ('fechaCompra', models.DateField(verbose_name='Fecha Compra')),
                ('estadoCompra', models.CharField(default='', max_length=30, verbose_name='Estado de la Compra')),
                ('comprobante_number', models.CharField(default='', max_length=50, verbose_name='Numero de comprobante')),
                ('idComprobante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense_manager.comprobantepago', verbose_name='Identificador de Comprobante de Pago')),
                ('idPersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Indicador de la Persona')),
                ('idProductos', models.ManyToManyField(to='products.Producto', verbose_name='Indicador del Producto')),
                ('idTipoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense_manager.tipopago', verbose_name='Identificador de tipo de Pago')),
            ],
            options={
                'verbose_name': 'Detalles de la compra',
            },
        ),
    ]
