from rest_framework import serializers
from messaging.models import User, Message, MessageHistory, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageHistory
        fields = [
            'id',
            'content'
            'edited_by',
            'edited_at'
        ]


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)
    receiver = serializers.PrimaryKeyRelatedField(read_only=True)
    message_history = MessageHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'content'
            'timestamp'
            'edited'
        ]


class NotificationSerializer(serializers.ModelSerializer):
    receiver = serializers.PrimaryKeyRelatedField(read_only=True)
    message = MessageSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id',
            'receiver',
            'message'
            'created_at'
        ]
