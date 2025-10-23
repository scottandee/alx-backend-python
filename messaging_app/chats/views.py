from rest_framework import viewsets, status, filters
from chats.serializers import ConversationSerializer, MessageSerializer
from chats.models import Conversation, Message


class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations on conversation entities
    """
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
    filter_backends = [filters.SearchFilter]

class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations on message entities
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        # Automatically assign the sender to the current user
        message = serializer.save(sender=self.request.user)

        conversation = message.conversation
        if self.request.user not in conversation.participants.all():
            conversation.participants.add(self.request.user)
            conversation.save()