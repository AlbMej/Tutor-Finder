# chat/routing.py
#copy/pasted from: https://channels.readthedocs.io/en/latest/tutorial/part_2.html
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
