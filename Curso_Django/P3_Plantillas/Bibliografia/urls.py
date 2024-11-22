from django.urls import path
from Bibliografia import views


urlpatterns=[
    path("",views.index, name='index'),
    path("deportes",views.deportes, name='deportes')
]