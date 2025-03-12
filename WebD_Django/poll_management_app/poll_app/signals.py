from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vote

@receiver(post_save, sender=Vote)
def log_vote(sender, instance, created, **kwargs):
    if created:
        print(f"New vote recorded: {instance.choice} by {instance.user}")