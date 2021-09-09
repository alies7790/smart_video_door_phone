from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import api

app_name='controllerModules'
urlpatterns=[
 path('open_door/', api.openDoor.as_view(), name='بازکردن درب'),
]