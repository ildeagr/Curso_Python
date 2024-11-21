from django.urls import path

from marketing import views

urlpatterns=[
    path('',views.index,name='index'),
    path('datos',views.datos,name='message')
]