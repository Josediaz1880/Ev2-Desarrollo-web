from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Ingresar proveedor"
        verbose_name_plural = "Ingresar proveedores"

    def __str__(self):
        return self.nombre


""" --------------------------------------------------- """


class categorias(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


""" --------------------------------------------------- """
class productos(models.Model):
    nombre = models.CharField(max_length=50)
    valor_unitario = models.IntegerField()
    categoria =models.ForeignKey(categorias,on_delete=models.CASCADE,null=True)
    proveedor = models.ForeignKey(proveedores, on_delete=models.CASCADE,null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre

""" --------------------------------------------------- """

class sucursales(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=12)
    responsable = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "sucursal"
        verbose_name_plural = "sucursales"

    def __str__(self):
        return self.nombre

""" --------------------------------------------------- """
class proveedor_producto(models.Model):
    proveedor = models.ForeignKey(proveedores, on_delete=models.CASCADE)
    producto = models.ForeignKey(productos, on_delete=models.CASCADE)


""" --------------------------------------------------- """


class entradaMercancia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(productos, null=True, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(sucursales, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Entrada mercancía"
        verbose_name_plural = "Entradas mercancía"

    def __str__(self):
        return str(self.fecha)

    def save(self, *args, **kwargs):
        self.fecha = timezone.now()  # Establecer la fecha con el tiempo actual

        if self.cantidad is None:
            raise ValueError("La cantidad debe ser especificada.")

        # Verificar si el producto ya existe en el inventario de la sucursal
        producto_inv, created = producto_inventario.objects.get_or_create(producto=self.producto, inventario__sucursal=self.sucursal, cantidad=self.cantidad)

        if created:
            # Si el producto no existe, crear un nuevo registro en producto_inventario con la cantidad de entradaMercancia
            producto_inv = producto_inventario.objects.create(producto=self.producto, inventario__sucursal=self.sucursal, cantidad=self.cantidad)
        else:
            # Si el producto ya existe, sumar la cantidad de entradaMercancia a la cantidad existente en producto_inventario
            producto_inv.cantidad += self.cantidad
            producto_inv.save()

        super().save(*args, **kwargs)


""" --------------------------------------------------- """
class salidaMercancia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(productos, null=True, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(sucursales, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Salida mercancía"
        verbose_name_plural = "Salida mercancías"

    def __str__(self):
        return str(self.fecha)

    def save(self, *args, **kwargs):
        self.fecha = timezone.now()  # Establecer la fecha con el tiempo actual

        if self.cantidad is None:
            raise ValueError("La cantidad debe ser especificada.")

        # Verificar si el producto ya existe en el inventario de la sucursal
        producto_inv = producto_inventario.objects.filter(producto=self.producto, inventario__sucursal=self.sucursal).first()

        if producto_inv:
            # Comprobar si hay suficiente cantidad en el inventario para la salida
            if producto_inv.cantidad >= self.cantidad:
                # Restar la cantidad de salidaMercancia a la cantidad existente en producto_inventario
                producto_inv.cantidad -= self.cantidad
                producto_inv.save()
            else:
                raise ValueError("No hay suficiente cantidad en el inventario para realizar la salida.")
        else:
            raise ValueError("El producto no existe en el inventario de la sucursal.")

        super().save(*args, **kwargs)
""" --------------------------------------------------- """

class devolucionMercancia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(productos, null=True, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(sucursales, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Devolución mercancía"
        verbose_name_plural = "Devolución mercancías"

    def __str__(self):
        return str(self.fecha)

    def save(self, *args, **kwargs):
        self.fecha = timezone.now()  # Establecer la fecha con el tiempo actual

        # Verificar si el producto ha sido previamente vendido
        if not salidaMercancia.objects.filter(producto=self.producto, sucursal=self.sucursal).exists():
            raise ValidationError("El producto no ha sido vendido previamente. No se puede realizar la devolución.")

        # Verificar si el producto existe en el inventario de la sucursal
        producto_inv = producto_inventario.objects.get(producto=self.producto, inventario__sucursal=self.sucursal)

        # Sumar la cantidad devuelta en devolucionMercancia a la cantidad existente en producto_inventario
        producto_inv.cantidad += self.cantidad
        producto_inv.save()

        super().save(*args, **kwargs)

""" --------------------------------------------------- """

class roles(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)

    class Meta:
        verbose_name = "permiso"
        verbose_name_plural = "permisos"

    def __str__(self):
        return self.nombre



""" --------------------------------------------------- """


class inventario(models.Model):
    cantidad_maxima = models.IntegerField(null=True)
    cantidad_minima = models.IntegerField(null=True)
    sucursal = models.ForeignKey(sucursales, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "inventario"
        verbose_name_plural = "inventarios"

    def __str__(self):
        return str(self.cantidad_maxima)

""" --------------------------------------------------- """


class producto_inventario(models.Model):
    cantidad = models.IntegerField()
    inventario = models.ForeignKey(inventario, on_delete=models.CASCADE)
    producto = models.ForeignKey(productos, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "inventario"
        verbose_name_plural = "inventarios"

    def __str__(self):
        return str(self.cantidad)


""" --------------------------------------------------- """


