from django.urls import path
from CV import views

urlpatterns=[
    path("", views.infocv ,name = 'infocv')
]