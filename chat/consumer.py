import json
from channels.generic.websocket import WebsocketConsumer

class chatConsumer(WebsocketConsumer):
    def connect(self):
        self.accpet()
        self.send(text_data=json.dumps(
            {
                'text':'connection established',
                'message':'you are now connected'
            }
        ))