# Generated by Django 3.2.9 on 2022-06-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220624_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproducto',
            name='estadoPromocion',
            field=models.CharField(default='NOP', max_length=15, verbose_name='Estado de la Promocion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='estadoPromocion',
            field=models.CharField(default='NOP', max_length=15, verbose_name='Estado de la Promocion'),
        ),
    ]
