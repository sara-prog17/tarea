# Generated by Django 4.1.3 on 2022-11-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='n_pedido',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
