from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

from doorSecurity import routing as doorSeurity_routing

application =ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            doorSeurity_routing.websocket_urlpatterns
        )
    )
})