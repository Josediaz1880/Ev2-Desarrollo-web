from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from inventarioApp.models import *
from django.contrib.contenttypes.models import ContentType


class CustomUser(AbstractUser):
    # Agrega campos adicionales según sea necesario
    nombre_completo = models.CharField(max_length=70)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    sucursal = models.ForeignKey(sucursales, on_delete=models.CASCADE)
    rol = models.ForeignKey(roles, on_delete=models.CASCADE)
    tipo_permisos_choices =(
        (0, 'Administrador'),
        (1, 'Gestión de proveedores'),
        (2, 'Gestión de movimientos'),
    )
    tipo_permisos=models.IntegerField(choices=tipo_permisos_choices, default=0)
    # Define campos de autenticación
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.username


class Permiso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"

    def __str__(self):
        return self.nombre


def create_permissions(sender, **kwargs):
    if kwargs['created']:
        content_type = ContentType.objects.get_for_model(Permiso)

        permiso_crear_sucursal = Permission.objects.create(
            name='Crear sucursal',
            codename='add_sucursales',
            content_type=content_type
        )
        permiso_editar_sucursal = Permission.objects.create(
            name='Editar sucursal',
            codename='change_sucursales',
            content_type=content_type
        )
        permiso_eliminar_sucursal = Permission.objects.create(
            name='Eliminar sucursal',
            codename='delete_sucursales',
            content_type=content_type
        )

        permiso_crear_usuario = Permission.objects.create(
            name='Crear usuario',
            codename='add_CustomUser',
            content_type=content_type
        )
        permiso_editar_usuario = Permission.objects.create(
            name='Editar usuario',
            codename='change_CustomUser',
            content_type=content_type
        )

        permiso_crear_rol = Permission.objects.create(
            name='Crear Rol',
            codename='add_roles',
            content_type=content_type
        )
        permiso_editar_rol = Permission.objects.create(
            name='Editar Rol',
            codename='change_roles',
            content_type=content_type
        )
        permiso_eliminar_rol = Permission.objects.create(
            name='Eliminar Rol',
            codename='delete_roles',
            content_type=content_type
        )

        permiso_crear_inventario = Permission.objects.create(
            name='Crear inventario',
            codename='add_inventario',
            content_type=content_type
        )
        permiso_editar_inventario = Permission.objects.create(
            name='Editar inventario',
            codename='change_inventario',
            content_type=content_type
        )

        permiso_crear_proveedor = Permission.objects.create(
            name='Crear proveedor',
            codename='add_proveedores',
            content_type=content_type
        )
        permiso_editar_proveedor = Permission.objects.create(
            name='Editar proveedor',
            codename='change_proveedores',
            content_type=content_type
        )
        permiso_eliminar_proveedor = Permission.objects.create(
            name='Eliminar proveedor',
            codename='delete_proveedores',
            content_type=content_type
        )

        permiso_crear_producto = Permission.objects.create(
            name='Crear producto',
            codename='add_productos',
            content_type=content_type
        )
        permiso_editar_producto = Permission.objects.create(
            name='Editar producto',
            codename='change_productos',
            content_type=content_type
        )
        permiso_eliminar_producto = Permission.objects.create(
            name='Eliminar producto',
            codename='delete_productos',
            content_type=content_type
        )

        permiso_crear_salida = Permission.objects.create(
            name='Crear salida',
            codename='add_salidaMercancia',
            content_type=content_type
        )
        permiso_editar_salida = Permission.objects.create(
            name='Editar salida',
            codename='change_salidaMercancia',
            content_type=content_type
        )

        permiso_crear_entrada = Permission.objects.create(
            name='Crear entrada',
            codename='add_entradaMercancia',
            content_type=content_type
        )
        permiso_editar_entrada = Permission.objects.create(
            name='Editar entrada',
            codename='change_entradaMercancia',
            content_type=content_type
        )

        permiso_crear_devolucion = Permission.objects.create(
            name='Crear devolucion',
            codename='add_devolucionMercancia',
            content_type=content_type
        )
        permiso_editar_devolucion = Permission.objects.create(
            name='Editar devolucion',
            codename='change_devolucionMercancia',
            content_type=content_type
        )

        permiso_generar_reporte = Permission.objects.create(
            name='Generar reporte',
            content_type=content_type
        )

        grupo_administradores = Group.objects.create(name='Administradores')
        grupo_gestion_proveedores = Group.objects.create(
            name='Gestion Proveedores')
        grupo_gestion_movimientos = Group.objects.create(
            name='Gestion Movimientos')

        grupo_administradores.permissions.add(
            permiso_crear_sucursal,
            permiso_editar_sucursal,
            permiso_eliminar_sucursal,
            permiso_crear_usuario,
            permiso_editar_usuario,
            permiso_crear_rol,
            permiso_editar_rol,
            permiso_eliminar_rol,
            permiso_crear_producto,
            permiso_editar_producto,
            permiso_eliminar_producto,
            permiso_crear_salida,
            permiso_editar_salida,
            permiso_crear_entrada,
            permiso_editar_entrada,
            permiso_crear_devolucion,
            permiso_editar_devolucion,
            permiso_generar_reporte
        )


        grupo_administradores.save()


        grupo_gestion_proveedores.permissions.add(
            permiso_crear_producto,
            permiso_editar_producto,
            permiso_eliminar_producto,
            permiso_crear_proveedor,
            permiso_editar_proveedor,
            permiso_eliminar_proveedor
        )

        grupo_gestion_proveedores.save()

        grupo_gestion_movimientos.permissions.add(
            permiso_crear_salida,
            permiso_editar_salida,
            permiso_crear_entrada,
            permiso_editar_entrada,
            permiso_crear_devolucion,
            permiso_editar_devolucion
        )

        grupo_gestion_movimientos.save()

