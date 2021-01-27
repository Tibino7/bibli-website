from django.urls import path

from . import views

urlpatterns = [
    path('', views.table, name='detail'),
    path('insert', views.insert, name='insert'),
]