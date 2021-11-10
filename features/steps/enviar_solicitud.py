from behave import *
from django.contrib.auth.models import User
from apps.usuarios.models import Perfil
from django.forms import formset_factory
from apps.usuarios.forms import EnvioSolicitudForm
        
# Validación de campos obligatorios    
def is_none(cadena):
    if cadena == 'None':
        return None
    else:
        return cadena

@given('que el usuario ha suministrados los detalles de su cuenta de usuario de forma satisfactoria')
def step_impl(context):
    pass

@when('no selecciona al menos una Aspiración {aspiraciones}, {comentario}')
def step_impl(context, aspiraciones, comentario):
    data = {
         'form-TOTAL_FORMS': '1',
         'form-INITIAL_FORMS': '0',
         'form-MAX_NUM_FORMS': '',
         'form-0-aspiraciones': is_none(aspiraciones),
         'form-0-comentatio': is_none(comentario)
     }
    EnvioSolicitudFormSet = formset_factory(EnvioSolicitudForm)
    context.form_envio_solicitud = EnvioSolicitudFormSet (data)       
    pass    
    
@then('se emite un mensaje de error invitandolé a seleccionar una Aspiración')
def step_impl(context):
    centinela = True
    for form in context.form_envio_solicitud:
        print(form)
    
    for form in context.form_envio_solicitud:
        print(form.is_valid())
        print(form.errors)
    
    for form in context.form_envio_solicitud:
        print(form.cleaned_data)
        if form.is_valid() == False:
            centinela = False
    pass
        