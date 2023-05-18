from django.db import models
# Create your models here.
class proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)

    class Meta:
        verbose_name = "Ingresar proveedor"
        verbose_name_plural = "Ingresar proveedores"

    def __str__(self):
        return self.nombre


""" --------------------------------------------------- """

class productos(models.Model):
    nombre = models.CharField(max_length=50)
    valor_unitario = models.IntegerField()

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

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

    class Meta:
        verbose_name = "Entrada mercancía"
        verbose_name_plural = "Entrada mercancías"

    def __str__(self):
        return str(self.fecha)

""" --------------------------------------------------- """

class salidaMercancia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    class Meta:
        verbose_name = "Salida mercancía"
        verbose_name_plural = "Salida mercancías"

    def __str__(self):
        return str(self.fecha)

""" --------------------------------------------------- """

class devolucionMercancia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    class Meta:
        verbose_name = "Devolución mercancía"
        verbose_name_plural = "Devolución mercancías"

    def __str__(self):
        return str(self.fecha)

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

class sucursales(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=12)
    responsable = models.CharField(max_length=50)
    entrada = models.ForeignKey(entradaMercancia, on_delete=models.CASCADE)
    salida = models.ForeignKey(salidaMercancia, on_delete=models.CASCADE)
    devolucion = models.ForeignKey(devolucionMercancia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "sucursal"
        verbose_name_plural = "sucursales"

    def __str__(self):
        return self.nombre


""" --------------------------------------------------- """


class inventario(models.Model):
    cantidad_maxima = models.IntegerField(null=True)
    cantidad_minima = models.IntegerField(null=True)
    id_sucursal = models.ForeignKey(sucursales, on_delete=models.CASCADE)

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
