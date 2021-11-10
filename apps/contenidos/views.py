from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from apps.contenidos.forms import AreaDeSaberForm
from apps.contenidos.models import AreaDelSaber
from django.views import generic

class AreasSaberCreateView(generic.CreateView):
    model = AreaDelSaber
    form_class = AreaDeSaberForm
    template_name = 'platilla_gestion_areas_saber.html'
    success_url = reverse_lazy('contenidos:lista')

class AreasSaberCreateListView(generic.ListView):
    model = AreaDelSaber
    template_name = 'saber.html'
    context_object_name = 'saber'

class AreasSaberUpdate(generic.UpdateView):
	model = AreaDelSaber
	form_class = AreaDeSaberForm
	template_name = 'platilla_gestion_areas_saber.html'
	success_url = reverse_lazy('contenidos:lista')

class AreasSaberDelete(generic.DeleteView):
	model = AreaDelSaber
	template_name = 'saber_eliminar.html'
	success_url = reverse_lazy('contenidos:lista')