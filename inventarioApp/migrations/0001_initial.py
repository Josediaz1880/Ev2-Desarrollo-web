# Generated by Django 3.2.16 on 2023-05-09 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='devolucionMercancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Devolución mercancía',
                'verbose_name_plural': 'Devolución mercancías',
            },
        ),
        migrations.CreateModel(
            name='entradaMercancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Entrada mercancía',
                'verbose_name_plural': 'Entrada mercancías',
            },
        ),
        migrations.CreateModel(
            name='permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'permiso',
                'verbose_name_plural': 'permisos',
            },
        ),
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'Ingresar proveedor',
                'verbose_name_plural': 'Ingresar proveedores',
            },
        ),
        migrations.CreateModel(
            name='salidaMercancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Salida mercancía',
                'verbose_name_plural': 'Salida mercancías',
            },
        ),
        migrations.CreateModel(
            name='sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=12)),
                ('responsable', models.CharField(max_length=30)),
                ('id_devolucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.devolucionmercancia')),
                ('id_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.entradamercancia')),
                ('id_salida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.salidamercancia')),
            ],
            options={
                'verbose_name': 'sucursal',
                'verbose_name_plural': 'sucursales',
            },
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=30)),
                ('nombre_completo', models.CharField(max_length=70)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12)),
                ('id_permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.permisos')),
                ('id_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.sucursales')),
            ],
            options={
                'verbose_name': 'usuarios',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='mercancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.proveedores')),
                ('id_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.sucursales')),
            ],
            options={
                'verbose_name': 'mercancia',
                'verbose_name_plural': 'mercancias',
            },
        ),
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_mercancia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.mercancia')),
                ('id_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.sucursales')),
            ],
            options={
                'verbose_name': 'inventario',
                'verbose_name_plural': 'inventarios',
            },
        ),
    ]
