
# import RPi.GPIO as GPIO
import json

from rest_framework.response import Response
from rest_framework.views import APIView

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import  status
from . import schemas,serializers
from accounts.models import Profiles

class openDoor(APIView):
    schema = schemas.openDoor()
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile=Profiles.objects.get(user_id=request.user.id)
            channel_layer=get_channel_layer()
            group_name=f"controller_open_door_{profile.rasspery.token}"
            async_to_sync(channel_layer.group_send)(
                group_name,
                {
                    'type':'open_door',
                    'message': json.dumps({'order':'open_door'})
                })
        else:
            return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)



