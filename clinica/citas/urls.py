from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_citas, name='listar'),
    path('agregar/', views.agregar_cita, name='agregar'),
    path('editar/<int:id>/', views.editar_cita, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_cita, name='eliminar'),
    path('pdf/', views.generar_pdf, name='pdf'),
]
