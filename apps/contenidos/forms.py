from django import forms
from apps.contenidos.models import AreaDelSaber

class AreaDeSaberForm(forms.ModelForm):
    class Meta:
        model = AreaDelSaber
        fields = [
            'nombre',
            'descripcion',
            'ilustracion_primaria',
            'ilustracion_secundaria',
            'estado',
            'usuario',	
        ]
        labels = {
            'nombre':'Nombre Del Area',
            'descripcion':'Descripcion Del Area',
            'ilustracion_primaria':'Ilustracion Principal',
            'ilustracion_secundaria':'Ilustracion Secundaria',
            'estado':'Estado',
            'usuario':'Usuario',
            'fecha_de_registro':'Fecha de registro',
            'fecha_de_modificacion':'Fecha de modificación',
        }
        widgets = {
            'nombre':forms.TextInput(),
            'descripcion':forms.TextInput(),
            'ilustracion_primaria':forms.FileInput(),
            'ilustracion_secundaria':forms.FileInput(),
            'estado':forms.Select(),
            'usuario':forms.Select(),
        }