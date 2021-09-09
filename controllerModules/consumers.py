import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class openDoorCunsumer(WebsocketConsumer):
    def connect(self):
        self.token=str(dict(self.scope['headers'])[b'token'])
        self.token=self.token[2:len(self.token)-1]
        self.group_name=f"controller_open_door_{self.token}"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.group_name,
            self.channel_layer
        )

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send('ssss')
            self.group_name = f"controller_open_door_{self.token}"
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'open_door',
                    'message': json.dumps({'order':'open_door'})
                })
    def open_door(self,event):
        message=event['message']
        self.send(text_data=message)