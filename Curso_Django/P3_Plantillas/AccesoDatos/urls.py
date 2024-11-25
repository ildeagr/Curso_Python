from django.urls import path

from AccesoDatos import views

urlpatterns=[
    path('',views.index,name='index')
]
