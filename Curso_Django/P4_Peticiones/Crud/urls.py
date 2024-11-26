from django.urls import path

from Crud import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peticion', views.peticion, name='peticion'),
    path('insert', views.insert, name='insert'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]