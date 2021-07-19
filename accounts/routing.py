
from  django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('kirivaslshod/',consumers.EchoCunsumer.as_asgi(),name ='تست')

]