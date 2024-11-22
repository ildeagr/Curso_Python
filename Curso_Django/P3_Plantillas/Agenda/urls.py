from django.urls import path
from Agenda import views


urlpatterns = [
    path("cliente", views.agenda, name = 'agenda')
]