from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.models import User
from .models import Perfil, TipoDeDisponibilidad, EstadoDeAcceso, TipoDePrivilegios, EstadoDeSolicitud, Solicitud
from .forms import RegistroUsuarioForm, RegistroPerfilForm, EnvioSolicitudForm, LoginForm

class SolicitudCreate(generic.CreateView):
    model = Perfil
    template_name = 'general_usuario.html'
    form_class = RegistroUsuarioForm
    second_form_class = RegistroPerfilForm
    third_form_class = EnvioSolicitudForm
    success_url = "/usuarios/"
    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)    
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST, request.FILES)
        form3 = self.third_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            user = form.save(commit=False)
            user.save()
            perfil = form2.save(commit=False)
            perfil.disponibilidad = TipoDeDisponibilidad.objects.get(id=1)
            perfil.estado_de_acceso = EstadoDeAcceso.objects.get(id=1)
            perfil.usuario = user
            perfil.save()
            solicitud = form3.save(commit=False)
            solicitud.solicitante = user
            solicitud.estado = EstadoDeSolicitud.objects.get(id=1)
            solicitud.set_fecha_de_envio()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))    
    
class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'inicio_de_sesion.html'
    success_url = reverse_lazy('panel-de-inicio')


def buscar_usuario(request, nombre):
    usuario = get_object_or_404(User, username=nombre)
    data = {
        'username': usuario.username,
        'firstName': usuario.first_name,
        'lastName': usuario.last_name,
        'password': usuario.password
    }

    return JsonResponse(data)
