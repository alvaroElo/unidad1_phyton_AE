from django import forms
from .models import Dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo  # modelo asociado
        fields = '__all__'  # todos los campos o una lista ['nombre', 'categoria', 'zona', 'consumo_maximo', 'estado']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # valor ingresado por el usuario cleaned_data es un diccionario para acceder a los datos limpios

        if len(nombre) < 3:  # validación personalizada cantidad mínima de caracteres
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')  # lanza error si no cumple

        return nombre
