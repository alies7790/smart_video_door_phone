from  django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/open_door_websocket/',consumers.openDoorCunsumer.as_asgi(),name ='ساکت باز کردن درب')

]