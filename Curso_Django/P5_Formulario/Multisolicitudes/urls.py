from django.urls import path

from Multisolicitudes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peticion', views.peticion, name='peticion'),
]