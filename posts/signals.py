from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from .services import send_mails_to_followers


@receiver(post_save, sender=Post)
def notify_followers(sender, instance, created, **kwargs):
    if created:
        send_mails_to_followers(instance.get_absolute_url(), instance.author_id)


