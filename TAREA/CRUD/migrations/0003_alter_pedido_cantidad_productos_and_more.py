# Generated by Django 4.1.3 on 2022-11-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0002_alter_pedido_n_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cantidad_productos',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='incremento',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='n_pedido',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='producto_mas_transporte',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='proveedor',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tamaño_producto',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tiempo_entrega',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_producto',
            field=models.CharField(max_length=500),
        ),
    ]
