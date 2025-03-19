import logging
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Vote


logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """Logs when a user logs in."""
    print("User logged in")
    logger.info(f"User {user.username} logged in")