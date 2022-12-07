# Generated by Django 4.1.3 on 2022-11-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0005_rename_f_nacimentio_cliente_f_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ciud_residencia',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='l_exp_documento',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cantidad_productos',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='incremento',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='n_pedido',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='producto_mas_transporte',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='productos',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='proveedor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tamaño_producto',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tiempo_entrega',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_producto',
            field=models.CharField(max_length=6),
        ),
    ]