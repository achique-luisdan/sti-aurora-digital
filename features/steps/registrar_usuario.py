from behave import *
from django.contrib.auth.models import User
from apps.usuarios.models import Perfil
from django.forms import formset_factory
from apps.usuarios.forms import RegistroUsuarioForm, RegistroPerfilForm
        
# Validación de campos obligatorios    
def is_none(cadena):
    if cadena == 'None':
        return None
    else:
        return cadena

@given('que el Usuario ha seleccionado la opción registrarse')
def step_impl(context):
    pass

@when('le falto completar algún campo obligatorio ({username}, {first_name}, {last_name}, {email}, {imagen_de_perfil}, {sexo}, {fecha_de_nacimiento}, {password1}, {password2})')
def step_impl(context, username, first_name, last_name, email, imagen_de_perfil, sexo, fecha_de_nacimiento, password1, password2 ):
    data = {
         'form-TOTAL_FORMS': '1',
         'form-INITIAL_FORMS': '0',
         'form-MAX_NUM_FORMS': '',
         'form-0-username': is_none(username),
         'form-0-first_name': is_none(first_name),
         'form-0-last_name': is_none(last_name),
         'form-0-email': is_none(email),
         'form-0-password1': is_none(password1),
         'form-0-password2': is_none(password2),
     }
     
    data_2 = {
         'form-TOTAL_FORMS': '1',
         'form-INITIAL_FORMS': '0',
         'form-MAX_NUM_FORMS': '',
         'form-0-imagen_de_perfil': is_none(imagen_de_perfil),
         'form-0-sexo': is_none(sexo),
         'form-0-fecha_de_nacimiento':is_none(fecha_de_nacimiento),
     }

    RegistroUsuarioFormSet = formset_factory(RegistroUsuarioForm)
    context.form_registro_usuario = RegistroUsuarioFormSet (data)
    
    RegistroPerfilFormSet = formset_factory(RegistroPerfilForm)
    context.form_registro_perfil = RegistroPerfilFormSet (data_2)       
    pass    
    
@then('se emite un mensaje de error con el campo incompleto ("{mensaje}")')
def step_impl(context, mensaje):
    bandera_1 = True
    bandera_2 = True
    centinela = True
    for form in context.form_registro_usuario:
        print(form.is_valid())
        print(form.errors)
    
    for form in context.form_registro_usuario:
        print(form.cleaned_data)
        if form.is_valid() == False:
            bandera_1 = False
        
    for form in context.form_registro_perfil:
        print(form.is_valid())
        print(form.errors)
    
    for form in context.form_registro_perfil:
        print(form.cleaned_data)
        if form.is_valid() == False:
            bandera_2 = False
    if bandera_1 is False or bandera_2 is False:
        centinela = False
    if bandera_1 is True and bandera_2 is True:
        centinela = False  
    assert centinela is False
        