from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings

import requests


@receiver(post_save, sender=get_user_model())
def post_save_user(sender, instance, created, **kwargs):
    if created:
        requests.post(
            settings.MAILGUN_API_MESSAGE_URL,
            auth=("api", settings.MAILGUN_API_KEY),
            data={
                "from": settings.MAILGUN_SENDER_EMAIL,
                "to": [
                    instance.email,
                ],
                "subject": settings.MAILGUN_SUBJECT,
                "text": instance.username+settings.MAILGUN_TEXT,
            })
