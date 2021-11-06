import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from doorSecurity.models import InformationService
from rassperypiInfo.models import RassperySystem


class openDoorCunsumer(WebsocketConsumer):
    def connect(self):
        try:
            self.token=str(dict(self.scope['headers'])[b'token'])
            self.token=self.token[2:len(self.token)-1]
            self.serial_rasperyPi = str(dict(self.scope['headers'])[b'serial-rasperypi'])
            self.serial_rasperyPi = self.serial_rasperyPi[2:len(self.serial_rasperyPi) - 1]
        except:
            self.send("not serial-rasperypi &| token")
            self.disconnect(close_code=1)
        try:
            rassperypiInfo=RassperySystem.objects.get(hash_serial_rassperyPi=self.serial_rasperyPi , token_connect_rassperypi=self.token)
            rassperypiInfo.online_status=1
            rassperypiInfo.save()
            self.rassperypiInfo=rassperypiInfo
        except:
            self.send("not rassperyPi with informathons")
            self.disconnect(close_code=1)
        self.rassperypiInfo.online_status=1
        self.rassperypiInfo.save()
        self.group_name=f"doorSecurity_{self.serial_rasperyPi}"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
        try:
            informationService=InformationService.objects.get(rassperypiInfo=self.rassperypiInfo)
            self.send(json.dumps({'massege': 'change status openDoor', 'code': (1011 + informationService.status_opendoor)}))
        except:
            self.send("not rassperyPi with informathons")
            self.disconnect(close_code=1)

    def disconnect(self, close_code):
        self.rassperypiInfo.online_status=2
        self.rassperypiInfo.save()
        self.channel_layer.group_discard(
            self.group_name,
            self.channel_layer
        )

    def receive(self, text_data=None, bytes_data=None):
        if text_data:

            self.group_name = f"doorSecurity_{self.token}"
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'sendMassege',
                    'message': json.dumps({'order':'sendMassege'})
                })
    def sendMassege(self, event):
        message=event['message']
        self.send(text_data=message)