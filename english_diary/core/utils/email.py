from django.conf import settings

import requests


def send_email(*args, **kwargs):

    sender = kwargs.get("sender")
    receiver = kwargs.get("receiver")
    subject = kwargs.get("subject")
    text = kwargs.get("text")
    html = kwargs.get("html")

    response = requests.post(
        settings.MAILGUN_API_MESSAGE_URL,
        auth=("api", settings.MAILGUN_API_KEY),
        data={
            "from": sender,
            "to": [
                receiver,
            ],
            "subject": subject,
            "text": text,
            "html": html,
        })
    return response
