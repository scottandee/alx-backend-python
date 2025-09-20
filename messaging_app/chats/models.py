from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import datetime


class UserRole(models.TextChoices):
    GUEST = 'guest'
    HOST = 'host'
    ADMIN = 'admin'

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(null=False)
    last_name = models.CharField(null=False)
    email = models.EmailField(null=False, unique=True, db_index=True)
    password_hash = models.CharField(null=False)
    phone_number = models.CharField(null=True)
    role = models.CharField(choices=UserRole.choices, null=False)
    created_at = models.DateTimeField(default=datetime.now())

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message_body = models.TextField(null=False)
    sent_at = created_at = models.DateTimeField(default=datetime.now())

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
