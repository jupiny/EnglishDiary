from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from celery import Task

from core.utils.email import send_email


class SendWriteDiaryEmailTask(Task):

    def run(self):
        for user in get_user_model().objects.agree_email_notification():
            if not user.today_diary and user.email:
                send_email(
                    sender=settings.ADMIN_SENDER_EMAIL,
                    receiver=user.email,
                    subject=settings.WRITE_DIARY_EMAIL_SUBJECT.format(
                        username=user.username,
                    ),
                    text=settings.WRITE_DIARY_EMAIL_TEXT.format(
                        username=user.username,
                    ),
                    html=render_to_string(
                        "emails/write_diary.html",
                        context={
                            "username": user.username,
                            "diaries_count": user.diary_set.count(),
                            "words_count": user.distinct_whole_used_words_count(),
                        },
                    ),
                )
