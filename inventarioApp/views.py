from django.shortcuts import render, redirect
from inventarioApp.models import *
from accounts.models import *
from inventarioApp.forms import *
from django.db.models import Q
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib import styles
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter



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












""" ----------------------------------------------------------------- """

def generar_informe(request):
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            incluir_entradas = form.cleaned_data['incluir_entradas']
            incluir_salidas = form.cleaned_data['incluir_salidas']
            incluir_devoluciones = form.cleaned_data['incluir_devoluciones']
            incluir_productos = form.cleaned_data['incluir_productos']
            incluir_sucursales = form.cleaned_data['incluir_sucursales']

            # Verificar si no se seleccionó ninguna casilla
            if not (incluir_entradas or incluir_salidas or incluir_devoluciones or incluir_productos or incluir_sucursales):
                return render(request, 'gestion/generar_informe.html', {'form': form, 'mensaje': 'No se seleccionaron datos para generar el informe'})

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

            p = canvas.Canvas(response)

            y = 700  # Posición vertical inicial
            espaciado = 50
            espacio_columna = 20

            # Definir estilos de fuente
            bold_style = styles.getSampleStyleSheet().get('BodyText')
            bold_style.fontName = 'Helvetica-Bold'
            normal_style = styles.getSampleStyleSheet().get('BodyText')

            if incluir_entradas:
                entradas = entradaMercancia.objects.all()
                # Agregar lógica para escribir los datos de entradas en el informe
                p.setFont(normal_style.fontName, 13)
                p.drawString(100, y, "Datos de Entradas:")
                y -= 20

                # Dibujar encabezado de columnas
                # Establecer estilo de fuente normal
                p.setFont(normal_style.fontName, 10)
                p.drawString(100, y, "#")
                p.drawString(115, y, "Producto")
                p.drawString(180, y, "Cantidad")
                p.drawString(250, y, "Fecha")
                y -= espacio_columna

                for entrada in entradas:
                    p.drawString(100, y, str(entrada.id))
                    p.drawString(115, y, str(entrada.producto))
                    p.drawString(180, y, str(entrada.cantidad))
                    p.drawString(220, y, str(entrada.fecha))
                    y -= 20
                y -= 20
                p.drawString(220, y, str())
                    

            if incluir_salidas:
                salidas = salidaMercancia.objects.all()
                # Agregar lógica para escribir los datos de salidas en el informe
                p.setFont(normal_style.fontName, 13)
                p.drawString(100, y, "Datos de Salidas:")
                y -= 20

                # Dibujar encabezado de columnas
                # Establecer estilo de fuente normal
                p.setFont(normal_style.fontName, 10)
                p.drawString(100, y, "#")
                p.drawString(115, y, "Producto")
                p.drawString(180, y, "Cantidad")
                p.drawString(250, y, "Fecha")
                y -= espacio_columna

                for salida in salidas:
                    p.drawString(100, y, str(salida.id))
                    p.drawString(115, y, str(salida.producto))
                    p.drawString(180, y, str(salida.cantidad))
                    p.drawString(220, y, str(salida.fecha))
                    y -=20
                y -= 20
                p.drawString(220, y, str())

            if incluir_devoluciones:
                devoluciones = devolucionMercancia.objects.all()
                # Agregar lógica para escribir los datos de devoluciones en el informe
                p.setFont(normal_style.fontName, 13)
                p.drawString(100, y, "Datos de Devoluciones:")
                y -= 20

                # Dibujar encabezado de columnas
                # Establecer estilo de fuente normal
                p.setFont(normal_style.fontName, 10)
                p.drawString(100, y, "#")
                p.drawString(115, y, "Producto")
                p.drawString(180, y, "Cantidad")
                p.drawString(250, y, "Fecha")
                y -= espacio_columna

                for devolucion in devoluciones:
                    p.drawString(100, y, str(devolucion.id))
                    p.drawString(115, y, str(devolucion.producto))
                    p.drawString(180, y, str(devolucion.cantidad))
                    p.drawString(220, y, str(devolucion.fecha))
                    y -= 20
                y -= 20
                p.drawString(220, y, str())

            if incluir_productos:
                productos_lists = productos.objects.all()
                # Agregar lógica para escribir los datos de devoluciones en el informe
                p.setFont(normal_style.fontName, 13)
                p.drawString(100, y, "Datos de Productos:")
                y -= 20

                p.setFont(normal_style.fontName, 10)
                p.drawString(100, y, "#")
                p.drawString(115, y, "Nombre")
                p.drawString(180, y, "Valor unitario")
                y -= espacio_columna

                for productos_list in productos_lists:
                    p.drawString(100, y, str(productos_list.id))
                    p.drawString(115, y, str(productos_list.nombre))
                    p.drawString(180, y, str(productos_list.valor_unitario))
                    y -= 20
                y -= 20
                p.drawString(220, y, str())

            if incluir_sucursales:
                sucursales_lists = sucursales.objects.all()
                # Agregar lógica para escribir los datos de devoluciones en el informe
                p.setFont(normal_style.fontName, 13)
                p.drawString(100, y, "Datos de Sucursales:")
                y -= 20

                p.setFont(normal_style.fontName, 10)
                p.drawString(100, y, "id")
                p.drawString(115, y, "Nombre")
                p.drawString(200, y, "# entrada")
                p.drawString(250, y, "# salida")
                p.drawString(300, y, "# devolución")
                y -= espacio_columna

                for sucursales_list in sucursales_lists:
                    p.drawString(100, y, str(sucursales_list.id))
                    p.drawString(115, y, str(sucursales_list.nombre))
                    p.drawString(200, y, str(sucursales_list.entrada_id))
                    p.drawString(250, y, str(sucursales_list.salida_id))
                    p.drawString(300, y, str(sucursales_list.devolucion_id))
                    y -= 20
                y -= 20
                p.drawString(220, y, str())

            p.showPage()
            p.save()

            return response
    else:
        form = InformeForm()

    return render(request, 'gestion/generar_informe.html', {'form': form})


""" ----------------------------------------------------------------- """
