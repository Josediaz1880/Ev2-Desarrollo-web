# Generated by Django 3.2.16 on 2023-07-02 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0017_alter_entradamercancia_sucursal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='id_sucursal',
            new_name='sucursal',
        ),
    ]