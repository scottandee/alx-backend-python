from django.db.models.signals import post_save
from django.dispatch import receiver
from messaging.models import Message, Notification


@receiver(post_save, sender=Message, dispatch_uid='create_notification')
def create_notification(sender, instance, created, **kwargs):
    """Create a new notification when a new message is created"""
    print('message created')
    if created:
        notification = Notification.objects.create(
            recipient=instance.recipient, message=instance,
        )
