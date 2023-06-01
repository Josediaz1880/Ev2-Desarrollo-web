from django.shortcuts import render, redirect
from inventarioApp.models import *
from accounts.models import *
from inventarioApp.forms import *
from django.db.models import Q


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


""" ----------------------------------------------------------------- """
def crearEntrada(request):
    form = entradaForm()
    if (request.method == 'POST'):
        form = entradaForm(request.POST)
        if form.is_valid():
            ent = form.cleaned_data
            print(ent)
            print("datos validos")
            form.save()
            form = ''
            return redirect("/entradas")
    data = {'form': form, 'titulo': 'Ingresar entrada de productos'}
    return render(request, 'gestion/crearEntrada.html', data)


def editarEntrada(request, id):
    entrada = entradaMercancia.objects.get(id=id)
    data = {
        'form': entradaForm(instance=entrada),
        'titulo': 'Editar entrada de mercancía'
    }
    if (request.method == 'POST'):
        form = entradaForm(request.POST, instance=entrada)
        if (form.is_valid()):
            form.save()
            return redirect("/entradas")
        else:
            data['form'] = form
    return render(request, 'gestion/crearEntrada.html', data)
""" ----------------------------------------------------------------- """


def crearSalida(request):
    form = salidaForm()
    if (request.method == 'POST'):
        form = salidaForm(request.POST)
        if form.is_valid():
            sal = form.cleaned_data
            print(sal)
            print("datos validos")
            form.save()
            form = ''
            return redirect("/salidas")
    data = {'form': form, 'titulo': 'Ingresar salida de productos'}
    return render(request, 'gestion/crearSalida.html', data)


def editarSalida(request, id):
    salida = salidaMercancia.objects.get(id=id)
    data = {
        'form': salidaForm(instance=salida),
        'titulo': 'Editar salida de mercancía'
    }
    if (request.method == 'POST'):
        form = salidaForm(request.POST, instance=salida)
        if (form.is_valid()):
            form.save()
            return redirect("/salidas")
        else:
            data['form'] = form
    return render(request, 'gestion/crearSalida.html', data)


""" ----------------------------------------------------------------- """
def crearDevolucion(request):
    form = devolucionForm()
    if (request.method == 'POST'):
        form = devolucionForm(request.POST)
        if form.is_valid():
            dev = form.cleaned_data
            print(dev)
            print("datos validos")
            form.save()
            form = ''
            return redirect("/devoluciones")
    data = {'form': form, 'titulo': 'Ingresar devolución de productos'}
    return render(request, 'gestion/crearDevolucion.html', data)


def editarDevolucion(request, id):
    devolucion = devolucionMercancia.objects.get(id=id)
    data = {
        'form': devolucionForm(instance=devolucion),
        'titulo': 'Editar devolución de mercancía'
    }
    if (request.method == 'POST'):
        form = devolucionForm(request.POST, instance=devolucion)
        if (form.is_valid()):
            form.save()
            return redirect("/devoluciones")
        else:
            data['form'] = form
    return render(request, 'gestion/crearDevolucion.html', data)


""" ----------------------------------------------------------------- """


def buscar(request):
    query = request.GET.get('q')

    resultados_salida = salidaMercancia.objects.filter(Q(cantidad__icontains=query) | Q(cantidad__contains=query))
    resultados_entrada = entradaMercancia.objects.filter(cantidad__icontains=query)
    resultados_devolucion = devolucionMercancia.objects.filter(cantidad__icontains=query)
    resultados_proveedor = proveedores.objects.filter(nombre__icontains=query)
    resultados_producto = productos.objects.filter(nombre__icontains=query)
    resultados_rol = roles.objects.filter(nombre__icontains=query)
    resultados_sucursal = sucursales.objects.filter(nombre__icontains=query)

    resultados = {
        'salida': resultados_salida,
        'entrada': resultados_entrada,
        'devolucion': resultados_devolucion,
        'proveedor': resultados_proveedor,
        'producto': resultados_producto,
        'rol': resultados_rol,
        'sucursal': resultados_sucursal
    }

    return render(request, 'gestion/resultado_busqueda.html', {'resultados': resultados})


""" ----------------------------------------------------------------- """
