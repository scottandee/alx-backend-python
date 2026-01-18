from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet, HealthCheckView

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path("", include(router.urls)),
    path("health/", HealthCheckView.as_view(), name="health"),
]