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
    first_name = models.CharField(null=False)
    last_name = models.CharField(null=False)
    email = models.EmailField(null=False, unique=True, db_index=True)
    password_hash = models.CharField(null=False)
    phone_number = models.CharField(null=True)
    role = models.CharField(choices=UserRole.choices, null=False)
    created_at = models.DateTimeField(db_default=models.functions.Now())


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(db_default=models.functions.Now())

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
    sent_at = models.DateTimeField(db_default=models.functions.Now())
