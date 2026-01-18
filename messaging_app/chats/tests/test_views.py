import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from chats.models import Conversation

User = get_user_model()

@pytest.mark.django_db
def test_authenticated_user_can_list_conversations():
    client = APIClient()

    user = User.objects.create_user(
        username="testuser",
        password="pass123"
    )

    conversation = Conversation.objects.create()
    conversation.participants.add(user)

    client.force_authenticate(user=user)
    response = client.get("/api/conversations/")

    assert response.status_code == status.HTTP_200_OK
