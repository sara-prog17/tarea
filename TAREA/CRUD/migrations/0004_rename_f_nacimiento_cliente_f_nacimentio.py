# Generated by Django 4.1.3 on 2022-11-16 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0003_alter_pedido_cantidad_productos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='f_nacimiento',
            new_name='f_nacimentio',
        ),
    ]
