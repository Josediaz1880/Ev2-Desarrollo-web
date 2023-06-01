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
""" ------------------------------------------------------------- """

class salidaForm(forms.Form):
    fecha = forms.DateTimeField(
        initial=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    cantidad = forms.IntegerField(widget=forms.IntegerField())

class salidaForm(forms.ModelForm):
    class Meta:
        model = salidaMercancia
        fields = '__all__'


""" ------------------------------------------------------------- """


class devolucionForm(forms.Form):
    fecha = forms.DateTimeField(
        initial=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    cantidad = forms.IntegerField(widget=forms.IntegerField())


class devolucionForm(forms.ModelForm):
    class Meta:
        model = devolucionMercancia
        fields = '__all__'


""" ------------------------------------------------------------- """
