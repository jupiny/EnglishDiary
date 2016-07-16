from django.conf import settings
from django.contrib.auth import get_user_model

from celery import Task

from users.utils.send_email import send_email


class SendEmailTask(Task):

    def run(self, user_id):
        user = get_user_model().objects.get(pk=user_id)
        send_email(
            sender=settings.MAILGUN_SENDER_EMAIL,
            receiver=user.email,
            subject=settings.MAILGUN_SUBJECT,
            text=user.username+settings.MAILGUN_TEXT,
        )
