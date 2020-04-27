"""
adapted from https://channels.readthedocs.io/en/latest/tutorial/part_2.html
tutor_finder/routing.py
make a websocket to route the channels (which is a package used by the chat)
"""
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
