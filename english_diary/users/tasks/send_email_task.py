from django.conf import settings
from django.contrib.auth import get_user_model

import requests
from celery import Task


class SendEmailTask(Task):

    def run(self, user_id):
        user = get_user_model().objects.get(pk=user_id)
        requests.post(
            settings.MAILGUN_API_MESSAGE_URL,
            auth=("api", settings.MAILGUN_API_KEY),
            data={
                "from": settings.MAILGUN_SENDER_EMAIL,
                "to": [
                    user.email,
                ],
                "subject": settings.MAILGUN_SUBJECT,
                "text": user.username+settings.MAILGUN_TEXT,
            })
