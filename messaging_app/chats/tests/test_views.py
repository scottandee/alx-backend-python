import pytest
from unittest.mock import patch, MagicMock
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
@patch("chats.models.Conversation.objects")
def test_authenticated_user_can_list_conversations(mock_conversation_objects):
    fake_user = MagicMock()
    fake_user.id = 1
    fake_user.username = "testuser"

    fake_conversation = MagicMock()
    fake_conversation.id = 1
    fake_conversation.participants.all.return_value = [fake_user]

    mock_queryset = MagicMock()
    mock_queryset.filter.return_value = [fake_conversation]
    mock_conversation_objects.filter.return_value = mock_queryset.filter.return_value

    client = APIClient()
    client.force_authenticate(user=fake_user)

    response = client.get("/api/conversations/")

    assert response.status_code == status.HTTP_200_OK
