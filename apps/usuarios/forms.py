from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.models import Perfil, Solicitud
from django.core.exceptions import ValidationError

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo Eléctronico',
        }
        widgets = {
            
        }          
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Los dos campos de contraseña no coinciden. [Validación personalizada]')
        return password2
            
class RegistroPerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('imagen_de_perfil', 'sexo', 'fecha_de_nacimiento')
        labels = {
            'imagen_de_perfil': 'Imagen de Perfil',
            'sexo':'Sexo',
            'fecha_de_nacimiento':"Fecha de Nacimiento",
        }
        widgets = {
            'imagen_de_perfil':forms.FileInput(),
            'fecha_de_nacimiento': forms.TextInput(attrs={'class':'datepicker'}),
            'sexo': forms.RadioSelect(),
        }
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['fecha_de_nacimiento'].required = True
        self.fields['sexo'].required = True

class EnvioSolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            'aspiraciones',
            'comentario',
        ]
        labels = {
            'aspiraciones': 'Solicitud:',
            'comentario':'¿Por qué?',
        }
        widgets = {
            'aspiraciones': forms.RadioSelect(),
            'comentario':forms.Textarea(attrs={'class':'materialize-textarea'}),
        }
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['aspiraciones'].required = True
        
class LoginForm(forms.Form):
    nombre = forms.CharField()
    clave = forms.CharField(widget=forms.PasswordInput)
  
    def clean_nombre(self):
        try:
            nombre = self.cleaned_data.get('nombre')
            usuario = Usuario.objects.get(nombre_de_usuario=nombre)
        except Usuario.DoesNotExist as e:
            raise forms.ValidationError('Este usuario no existe!')
        
        return nombre    
             
    def clean_clave(self):
        clave = self.cleaned_data.get('clave')
        nombre = self.cleaned_data.get('nombre')
        
        try:
            usuario = Usuario.objects.get(nombre_de_usuario=nombre)
        except Usuario.DoesNotExist as e:
            raise forms.ValidationError('Este usuario no existe!')
        
        if usuario.contrasea != clave:
            raise forms.ValidationError('Clave incorreta!')
        
        return clave