# Generated by Django 3.2.16 on 2023-05-16 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='id_permiso',
            new_name='rol',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='id_sucursal',
            new_name='sucursal',
        ),
    ]
