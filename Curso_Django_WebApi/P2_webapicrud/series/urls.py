from django.urls import path

from series import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insertserie', views.insertserie, name='insertserie'),
    path('updateserie', views.updateserie, name='updateserie'),
    path('selectserie', views.selectserie, name='selectserie'),

    path('selectper', views.selectper, name='selectper'),
    path('insertper', views.insertper, name='insertper'),

    path('indexserie', views.indexserie, name='indexserie'),
    path('indexupdateserie', views.indexupdateserie, name='indexupdateserie'),

    path('indexper', views.indexper, name='indexper'),
]