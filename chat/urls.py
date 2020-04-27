'''chat/urls.py
adapted from: https://channels.readthedocs.io/en/latest/tutorial/part_1.html
and https://channels.readthedocs.io/en/latest/tutorial/part_1.html
this where the urls for the chat rooms are stored'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room')
]
