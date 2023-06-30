"""inventarioProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventarioApp.views import *
from accounts.views import *
from django.views.defaults import page_not_found
from accounts.views import page_not_found as accounts_page_not_found
from inventarioApp.views import page_not_found as inventarioApp_page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', SignUpView.as_view(),name='signup'),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sucursales/', sucursales_list, name='sucursales'),
    path('sucursales/agregar/', crearSucursal, name='crearSucursal'),
    path('sucursales/editar/<int:id>/',editarSucursal, name='editarSucursal'),
    path('sucursales/eliminar/<int:id>/',eliminarSucursal, name='eliminarSucursal'),
    path('usuarios/', usuarios_list, name='usuarios'),
    path('usuarios/agregar/', crearUsuario, name='crearUsuario'),
    path('usuarios/editar/<int:id>/',editarUsuario, name='editarUsuario'),
    path('roles/', roles_list, name='roles'),
    path('inventarios/', inventarios_list, name='inventarios'),
    path('inventarios/agregar/', crearInventario, name='crearInventario'),
    path('inventarios/editar/<int:id>/', editarInventario, name='editarInventario'),
    path('proveedores/', proveedores_list, name='proveedores'),
    path('proveedores/agregar/', crearProveedor, name='crearProveedor'),
    path('proveedores/editar/<int:id>/', editarProveedor, name='editarProveedor'),
    path('proveedores/eliminar/<int:id>/',eliminarProveedor, name='eliminarProveedor'),
    path('productos/', productos_list, name='productos'),
    path('productos/agregar/', crearProducto, name='crearProducto'),
    path('productos/editar/<int:id>/', editarProducto, name='editarProducto'),
    path('productos/eliminar/<int:id>/',eliminarProducto, name='eliminarProducto'),
    path('salidas/', salidas_list, name='salidas'),
    path('salidas/agregar/', crearSalida, name='salida'),
    path('salidas/editar/<int:id>', editarSalida, name='editarSalida'),
    path('entradas/', entradas_list, name='entradas'),
    path('entradas/agregar/',crearEntrada, name='entrada'),
    path('entradas/editar/<int:id>', editarEntrada, name='editarEntrada'),
    path('devoluciones/', devoluciones_list, name='devoluciones'),
    path('devoluciones/agregar/', crearDevolucion, name='devolucion'),
    path('devoluciones/editar/<int:id>',editarDevolucion, name='editarDevolucion'),
    path('buscar/',buscar, name='buscar'),
    path('generar-informe/', generar_informe, name='generar_reporte'),
    path('access-denied/', access_denied, name='access_denied'),

    path('inventarioApp/404/', inventarioApp_page_not_found, name='inventarioApp_page_not_found'),
    path('accounts/404/', accounts_page_not_found, name='accounts_page_not_found'),


    ]
handler404 = 'inventarioApp.views.page_not_found'
