
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
                    'massage':json.dumps({'sender': 'sss', 'receiver': 'sss', 'text': 'ss'})
                })

            try:
                # GPIO.setmode(GPIO.BCM)
                # GPIO.setwarnings(False)
                # GPIO.setup(3, GPIO.OUT)
                # GPIO.output(3, GPIO.HIGH)
                # time.sleep(2)
                # GPIO.output(3, GPIO.LOW)
                return Response({"message": "open Door"}, status=status.HTTP_200_OK)
            except:
                return Response({"message": "not login for logout"}, status=status.HTTP_412_PRECONDITION_FAILED)
        else:
            return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)



