from django import forms 
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError

class entradaForm(forms.Form):
    fecha = forms.DateTimeField(initial=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    cantidad = forms.IntegerField(widget=forms.IntegerField())

class entradaForm(forms.ModelForm):
    class Meta:
        model = entradaMercancia
        fields = '__all__'
    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        producto = cleaned_data.get('producto')

        if not cantidad:
            self.add_error('cantidad', 'Este campo es obligatorio')
        if not producto:
            self.add_error('producto', 'Este campo es obligatorio')
""" ------------------------------------------------------------- """

class salidaForm(forms.Form):
    fecha = forms.DateTimeField(initial=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    cantidad = forms.IntegerField(widget=forms.IntegerField())

class salidaForm(forms.ModelForm):
    class Meta:
        model = salidaMercancia
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        producto = cleaned_data.get('producto')

        if not cantidad:
            self.add_error('cantidad', 'Este campo es obligatorio')
        if not producto:
            self.add_error('producto', 'Este campo es obligatorio')


""" ------------------------------------------------------------- """


class devolucionForm(forms.Form):
    fecha = forms.DateTimeField(initial=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    cantidad = forms.IntegerField(widget=forms.IntegerField())


class devolucionForm(forms.ModelForm):
    class Meta:
        model = devolucionMercancia
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        producto = cleaned_data.get('producto')

        if not cantidad:
            self.add_error('cantidad', 'Este campo es obligatorio')
        if not producto:
            self.add_error('producto', 'Este campo es obligatorio')


""" ------------------------------------------------------------- """


class sucursalForm(forms.Form):
    nombre = forms.CharField(widget=forms.CharField(max_length=50))
    direccion = forms.CharField(widget=forms.CharField(max_length=100))
    telefono = forms.CharField(widget=forms.CharField(max_length=12))
    responsable = forms.CharField(widget=forms.CharField(max_length=50))


class sucursalForm(forms.ModelForm):
    class Meta:
        model = sucursales
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        direccion = cleaned_data.get('direccion')
        telefono = cleaned_data.get('telefono')
        responsable = cleaned_data.get('responsable')

        if not nombre:
            self.add_error('nombre', 'Este campo es obligatorio')
        if not direccion:
            self.add_error('direccion', 'Este campo es obligatorio')
        if not telefono:
            self.add_error('telefono', 'Este campo es obligatorio')
        if not responsable:
            self.add_error('responsable', 'Este campo es obligatorio')



""" ------------------------------------------------------------- """


class inventarioForm(forms.Form):

    cantidad_maxima = forms.IntegerField(widget=forms.IntegerField())
    cantidad_minima = forms.IntegerField(widget=forms.IntegerField())

class inventarioForm(forms.ModelForm):
    class Meta:
        model = inventario
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        cantidad_maxima = cleaned_data.get('cantidad_maxima')
        cantidad_minima = cleaned_data.get('cantidad_minima')
        id_sucursal = cleaned_data.get('id_sucursal')

        if not cantidad_maxima:
            self.add_error('cantidad_maxima', 'Este campo es obligatorio')
        if not cantidad_minima:
            self.add_error('cantidad_minima', 'Este campo es obligatorio')

        if cantidad_maxima and cantidad_minima and cantidad_maxima <= cantidad_minima:
            raise ValidationError('La cantidad máxima debe ser mayor que la cantidad mínima.')

        if id_sucursal and inventario.objects.exclude(id=self.instance.id).filter(id_sucursal=id_sucursal).exists():
            raise ValidationError(
                'Ya existe un inventario asociado a esta sucursal.')


""" ------------------------------------------------------------- """


class inventoryForm(forms.Form):
    cantidad = forms.IntegerField(widget=forms.IntegerField())


class inventoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inventario'].label_from_instance = lambda obj: f"{obj.id_sucursal}"
    class Meta:
        model = producto_inventario
        fields = '__all__'



    def clean(self):
        cleaned_data = super().clean()
        inventario = cleaned_data.get('inventario')
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')

        if not cantidad:
            self.add_error('cantidad', 'Este campo es obligatorio')

        if inventario and producto:
            # Verificar si ya existe un registro con los mismos valores
            exists = producto_inventario.objects.filter(
                inventario_id=inventario, producto_id=producto).exists()
            if exists:
                self.add_error(
                    None, 'Este producto ya existe en el inventario.')

        return cleaned_data
""" ------------------------------------------------------------- """


class proveedorForm(forms.Form):
    nombre = forms.CharField(widget=forms.CharField(max_length=50))
    direccion = forms.CharField(widget=forms.CharField(max_length=100))
    telefono = forms.CharField(widget=forms.CharField(max_length=12))


class proveedorForm(forms.ModelForm):
    class Meta:
        model = proveedores
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        direccion = cleaned_data.get('direccion')
        telefono = cleaned_data.get('telefono')

        if not nombre:
            self.add_error('nombre', 'Este campo es obligatorio')
        if not direccion:
            self.add_error('direccion', 'Este campo es obligatorio')
        if not telefono:
            self.add_error('telefono', 'Este campo es obligatorio')


""" ------------------------------------------------------------- """


class productoForm(forms.Form):
    nombre = forms.CharField(widget=forms.CharField(max_length=50))
    valor_unitario = forms.IntegerField(widget=forms.IntegerField())


class productoForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        valor_unitario = cleaned_data.get('valor_unitario')

        if not nombre:
            self.add_error('nombre', 'Este campo es obligatorio')
        if not valor_unitario:
            self.add_error('valor_unitario', 'Este campo es obligatorio')


""" ------------------------------------------------------------- """


class categoriaForm(forms.Form):
    nombre = forms.CharField(widget=forms.CharField(max_length=50))
    descripcion = forms.CharField(widget=forms.CharField(max_length=150))

class categoriaForm(forms.ModelForm):
    class Meta:
        model = categorias
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')

        if not nombre:
            self.add_error('nombre', 'Este campo es obligatorio')

""" ------------------------------------------------------------- """

class InformeForm(forms.Form):
    incluir_entradas = forms.BooleanField(required=False)
    incluir_salidas = forms.BooleanField(required=False)
    incluir_devoluciones = forms.BooleanField(required=False)
    incluir_productos = forms.BooleanField(required=False)
    incluir_sucursales = forms.BooleanField(required=False)
    incluir_usuarios = forms.BooleanField(required=False)
