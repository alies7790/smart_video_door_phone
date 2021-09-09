from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

from controllerModules import routing as controllerModules_routing

application =ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            controllerModules_routing.websocket_urlpatterns
        )
    )
})