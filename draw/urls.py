# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('search', views.search, name='search'),
    path('repartee', views.repartee, name='repartee')
]
