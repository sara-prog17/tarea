# Generated by Django 4.1.3 on 2022-11-16 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0004_rename_f_nacimiento_cliente_f_nacimentio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='f_nacimentio',
            new_name='f_nacimiento',
        ),
    ]
