# Generated by Django 4.1.3 on 2022-11-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0013_alter_cliente_documento_alter_cliente_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.IntegerField(max_length=2),
        ),
    ]