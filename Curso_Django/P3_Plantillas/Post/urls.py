from django.urls import path

from Post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados', views.empleados, name='empleados'),
]