from django.urls import path

from Empleados import views

urlpatterns=[
    path('',views.index,name='index'),
    path('peliculas',views.index2,name='index2'),
    path('formulario',views.formulario,name='formulario')
]
