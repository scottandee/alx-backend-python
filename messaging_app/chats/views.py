from rest_framework import viewsets
from chats.serializers import ConversationSerializer, MessageSerializer
from chats.models import Conversation, Message


class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations on conversation entities
    """
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations on message entities
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
