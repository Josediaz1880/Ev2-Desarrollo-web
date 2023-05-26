from django import forms 
from django.forms import ModelForm
from .models import *


class entradaForm(forms.Form):
    fecha = forms.DateTimeField(initial=timezone.now().strftime("%Y-%m-%d %H:%M:%S"), widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))
    cantidad = forms.IntegerField()
    cantidad = forms.IntegerField(widget=forms.IntegerField())

    fecha.widget.attrs['disabled']='true'

class entradaForm(ModelForm):
    class Meta:
        model = entradaMercancia
        fields = '__all__'

    fecha = forms.DateTimeField()
    cantidad = forms.IntegerField()
""" ------------------------------------------------------------- """