# Generated by Django 4.1.3 on 2022-11-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0010_alter_cliente_celular_alter_cliente_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
