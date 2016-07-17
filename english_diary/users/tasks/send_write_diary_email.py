from django.conf import settings
from django.contrib.auth import get_user_model

from celery import Task

from users.utils.send_email import send_email


class SendWriteDiaryEmailTask(Task):

    def run(self):
        for user in get_user_model().objects.all():
            send_email(
                sender=settings.ADMIN_SENDER_EMAIL,
                receiver=user.email,
                subject=settings.WRITE_DIARY_EMAIL_SUBJECT.format(
                    username=user.username,
                ),
                text=settings.WRITE_DIARY_EMAIL_TEXT.format(
                    username=user.username,
                )
            )
