from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.SolicitudCreate.as_view(), name='panel-de-inicio'),
    path('login', views.LoginView.as_view(), name='login'),
    path('<str:nombre>', views.buscar_usuario, name='buscar-usuario')
]