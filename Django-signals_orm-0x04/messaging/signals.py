from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from messaging.models import Message, Notification, MessageHistory


@receiver(post_save, sender=Message, dispatch_uid='create_notification')
def create_notification(sender, instance, created, **kwargs):
    """Create a new notification when a new message is created"""
    if created:
        Notification.objects.create(
            receiver=instance.receiver,
            message=instance)


@receiver(pre_save, sender=Message, dispatch_uid='update_message_history')
def create_message_history(sender, instance, **kwargs):
    """Add to message history once a message is edited"""
    if not instance.pk:
        return

    try:
        old_instance = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return

    if old_instance.content != instance.content:
        MessageHistory.objects.create(
            message=instance, content=instance.content,
            edited_by=instance.sender,
        )
        instance.edited = True
