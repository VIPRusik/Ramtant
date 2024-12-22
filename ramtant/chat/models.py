from django.db import models

from users.models import Usr

class Message(models.Model):
    sender = models.ForeignKey(Usr, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Usr, related_name='received_messages', on_delete=models.CASCADE)

    content = models.TextField()
    
    timestamp = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.content}"