# chat/urls.py
#copy/pasted from: https://channels.readthedocs.io/en/latest/tutorial/part_1.html
#& https://channels.readthedocs.io/en/latest/tutorial/part_1.html
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room')
]
