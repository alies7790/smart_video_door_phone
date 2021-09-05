
# import RPi.GPIO as GPIO

from rest_framework.response import Response
from rest_framework.views import APIView

import time
from rest_framework import  status
from . import schemas,serializers

class openDoor(APIView):
    schema = schemas.openDoor()
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
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



