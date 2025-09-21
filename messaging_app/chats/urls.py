from rest_framework.routers import DefaultRouter
from chats.views import ConversationViewSet, MessageViewSet


router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = router.urls
