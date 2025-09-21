from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    phone_number = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            "user_id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "phone_number",
            "role",
            "created_at",
        ]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="sender", write_only=True
    )
    conversation_id = serializers.PrimaryKeyRelatedField(
        queryset=Conversation.objects.all(), source="conversation", write_only=True
    )
    sender = UserSerializer(read_only=True)
    conversation = serializers.UUIDField(source="conversation.conversation_id", read_only=True)

    class Meta:
        model = Message
        fields = [
            "message_id",
            "sender_id",
            "conversation_id",
            "sender",
            "conversation",
            "message_body",
            "sent_at",
        ]

    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), write_only=True
    )
    participants_details = UserSerializer(source="participants", many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            "conversation_id",
            "participants",
            "participants_details",
            "created_at",
            "messages",
        ]
