from django.shortcuts import render, redirect
from inventarioApp.models import *
from accounts.models import *
from inventarioApp.forms import *

def index(request):
    return render(request, 'sistema/index.html')


def sucursales_list(request):
    lista_sucursales = sucursales.objects.all()
    return render(request, 'registration/sucursales.html', {'lista_sucursales': lista_sucursales})


def usuarios_list(request):
    lista_usuarios = CustomUser.objects.all()
    return render(request, 'registration/usuarios.html', {'lista_usuarios': lista_usuarios})


def roles_list(request):
    lista_roles = roles.objects.all()
    return render(request, 'registration/roles.html', {'lista_roles': lista_roles})


def inventarios_list(request):
    lista_inventarios = inventario.objects.all()
    return render(request, 'registration/inventario.html', {'lista_inventarios': lista_inventarios})


def proveedores_list(request):
    lista_proveedores = proveedores.objects.all()
    return render(request, 'registration/proveedores.html', {'lista_proveedores': lista_proveedores})


def productos_list(request):
    lista_productos = productos.objects.all()
    return render(request, 'registration/productos.html', {'lista_productos': lista_productos})


def salidas_list(request):
    lista_salidas = salidaMercancia.objects.all()
    return render(request, 'registration/salidas.html', {'lista_salidas': lista_salidas})


def entradas_list(request):
    lista_entradas = entradaMercancia.objects.all()
    return render(request, 'registration/entradas.html', {'lista_entradas': lista_entradas})


def devoluciones_list(request):
    lista_devoluciones = devolucionMercancia.objects.all()
    return render(request, 'registration/devoluciones.html', {'lista_devoluciones': lista_devoluciones})


def crearEntrada(request):
    form = entradaForm()
    if (request.method == 'POST'):
        form = entradaForm(request.POST)
        if form.is_valid():
            ent = form.cleaned_data
            entrada = entradaForm(
                fecha=ent['nombre'],
                cantidad=ent['edad']
            )
            print("datos validos")
            entrada.save()
            form = ''
            return redirect("/entradas")
    data = {'form': form, 'titulo': 'Ingresar entrada de productos'}
    return render(request, 'gestion/crearEntrada.html', data)
