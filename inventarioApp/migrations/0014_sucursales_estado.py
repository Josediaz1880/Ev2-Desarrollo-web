# Generated by Django 3.2.16 on 2023-07-01 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0013_proveedores_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursales',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
