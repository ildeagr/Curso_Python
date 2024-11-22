from django.urls import path
from Deportes import views

urlpatterns=[
    path("", views.titular ,name = 'titular'),
    path("jugadores", views.jugadores, name='jugadores')
]