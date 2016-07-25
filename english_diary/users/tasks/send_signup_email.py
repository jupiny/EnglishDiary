from django.conf import settings
from django.contrib.auth import get_user_model

from celery import Task

from users.utils.send_email import send_email


class SendSignupEmailTask(Task):

    def run(self, user_id):
        user = get_user_model().objects.get(pk=user_id)
        if user.email:
            send_email(
                sender=settings.ADMIN_SENDER_EMAIL,
                receiver=user.email,
                subject=settings.SIGNUP_EMAIL_SUBJECT,
                text=settings.SIGNUP_EMAIL_TEXT.format(
                    username=user.username,
                )
            )
