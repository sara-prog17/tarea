# Generated by Django 4.1.3 on 2022-11-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0009_alter_cliente_documento_alter_cliente_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.IntegerField(),
        ),
    ]
