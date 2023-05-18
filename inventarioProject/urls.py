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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', SignUpView.as_view(),name='signup'),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sucursales/', sucursales_list, name='sucursales'),
    path('usuarios/', usuarios_list, name='usuarios'),
    path('roles/', roles_list, name='roles'),
    path('inventarios/', inventarios_list, name='inventarios'),
    path('proveedores/', proveedores_list, name='proveedores'),
    path('productos/', productos_list, name='productos'),
    path('salidas/', salidas_list, name='salidas'),
    path('entradas/', entradas_list, name='entradas'),
    path('devoluciones/', devoluciones_list, name='devoluciones'),
    ]
