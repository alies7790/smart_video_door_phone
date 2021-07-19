from channels.generic.websocket import WebsocketConsumer


class EchoCunsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data=text_data)
        if bytes_data:
            self.send(bytes_data=bytes_data)