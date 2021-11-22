"""
ASGI config for smart_video_door_phone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# import os
#
# import django
#
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from channels.routing import get_default_application
# from channels.auth import AuthMiddleware, AuthMiddlewareStack
# from websocketManage import routing as doorSeurity_routing
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_video_door_phone.settings')
# django.setup()
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             doorSeurity_routing.websocket_urlpatterns
#         )
#     )
# })



import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter, get_default_application
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_video_door_phone.settings')
django.setup()
django_asgi_app =get_default_application()
# django_asgi_app = get_asgi_application()
from channels.auth import AuthMiddleware, AuthMiddlewareStack
from websocketManage.routing import websocket_urlpatterns as doorSeurity_routing
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            doorSeurity_routing
        )
    )
})