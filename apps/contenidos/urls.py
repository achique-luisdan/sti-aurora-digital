from django.urls import path
from apps.contenidos.views import AreasSaberCreateView, AreasSaberCreateListView, AreasSaberUpdate, AreasSaberDelete
app_name= 'contenidos'

urlpatterns = [
    path('ingresar', AreasSaberCreateView.as_view(), name='ingresar'),
    path('ver', AreasSaberCreateListView.as_view(), name='lista'),
    path('editar/<int:pk>',AreasSaberUpdate.as_view(),name='editar'),
    path('eliminar/<int:pk>',AreasSaberDelete.as_view(),name='eliminar'),
]