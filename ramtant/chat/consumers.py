import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.username = self.scope["url_route"]["kwargs"]["username"]
        self.room_name = f"private_chat_{self.username}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )

    def receive(self, text_data):
        from users.models import Usr  # Отложенный импорт модели
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Здесь вы можете добавить логику работы с моделью Usr, если это нужно

        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({
            "message": message
        }))
