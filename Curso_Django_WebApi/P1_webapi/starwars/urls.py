from django.urls import path

from starwars import views

urlpatterns = [
    path('', views.index, name='index'),
]