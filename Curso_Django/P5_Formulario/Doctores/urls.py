from django.urls import path

from Doctores import views

urlpatterns = [
    path('formulario', views.formulario, name='formulario'),
    path('select', views.select, name='select')
]