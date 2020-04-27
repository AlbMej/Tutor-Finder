'''chat/consumers.py the page that deals with websockets and channels
adapted from the channels tutorial'''
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    '''the single class that creates and deals with all the sockets'''
    async def connect(self):
        '''when a user connects, need their username and roomname'''
        self.curr_user = str(self.scope['user'])
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        ''''User leaves the room'''
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        '''Receive message from WebSocket (got a message to send to the room)'''
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        #formatted as: "<user_name>: <message>"
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': self.curr_user + ': ' + message
            }
        )

    async def chat_message(self, event):
        '''Receive message from room group (got a message from the room)'''
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
