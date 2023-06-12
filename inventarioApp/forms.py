from django import forms 
from django.forms import ModelForm
from .models import *


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


class InformeForm(forms.Form):
    incluir_entradas = forms.BooleanField(required=False)
    incluir_salidas = forms.BooleanField(required=False)
    incluir_devoluciones = forms.BooleanField(required=False)
    incluir_productos = forms.BooleanField(required=False)
    incluir_sucursales = forms.BooleanField(required=False)
