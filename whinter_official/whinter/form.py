from django import forms
from .models import Sala

class SearchForm(forms.Form):
    name = forms.CharField(max_length=50,required=True, label='Ingresar nombre de usuario:')\
    

class CreateForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
        labels = {
            'nombre': 'Elegir un nombre para la Sala',
            'disponible': 'Disponible',
            'capacidad': 'Capacidad máxima',
            'descripcion': 'Descripción',
        }
