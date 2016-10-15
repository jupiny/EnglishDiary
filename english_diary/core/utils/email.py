from django.conf import settings

import requests


def send_email(sender, receiver, subject, html):
    response = requests.post(
        settings.MAILGUN_API_MESSAGE_URL,
        auth=("api", settings.MAILGUN_API_KEY),
        data={
            "from": sender,
            "to": [
                receiver,
            ],
            "subject": subject,
            "html": html,
        })
    return response
