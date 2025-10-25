from rest_framework import viewsets, status, filters
from chats.serializers import ConversationSerializer, MessageSerializer
from chats.models import Conversation, Message
from chats.permissions import IsParticipantOfConversation


class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations on conversation entities
    """
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        # Only show conversations the user participates in
        user = self.request.user
        return Conversation.objects.filter(participants=user)


class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations on message entities
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user)
    
    def perform_create(self, serializer):
        # Automatically assign the sender to the current user
        serializer.save(sender=self.request.user)
