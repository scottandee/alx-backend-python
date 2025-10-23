from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid
from datetime import datetime


class UserRole(models.TextChoices):
    GUEST = 'guest'
    HOST = 'host'
    ADMIN = 'admin'

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=False, unique=True, db_index=True)
    password_hash = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    role = models.CharField(choices=UserRole.choices, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    conversation = models.ForeignKey(
        Conversation,
        related_name="messages",
        on_delete=models.CASCADE,
        db_column="conversation_id",
    )
    sender = models.ForeignKey(
        User,
        related_name="messages",
        on_delete=models.CASCADE,
        db_column="sender_id",
    )
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)
