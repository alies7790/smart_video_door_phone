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
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_celery_heroku_project.settings')
django.setup()

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