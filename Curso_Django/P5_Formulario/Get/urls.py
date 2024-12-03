from django.urls import path

from Get import views

urlpatterns = [
    path('oficio', views.index, name='index'),
    path('empleados', views.empleados, name='empleados'),
]