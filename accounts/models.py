from django.db import models
from django.contrib.auth.models import AbstractUser
from inventarioApp.models import sucursales,roles
# Create your models here.


class CustomUser(AbstractUser):
    # Agrega campos adicionales según sea necesario
    nombre_completo = models.CharField(max_length=70)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    sucursal = models.ForeignKey(sucursales, on_delete=models.CASCADE)
    rol = models.ForeignKey(roles, on_delete=models.CASCADE)

    # Define campos de autenticación
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = "usuarios"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.username
