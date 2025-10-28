from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(null=False, unique=True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=100)

    def __str__(self):
        return f'User: {self.id}'

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.id} to {self.recipient.id}'

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    receiver = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Notification for {self.recipient.id}: {self.message.content}'

