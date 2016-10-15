from django.conf import settings

from celery import Task

from users.mixins import SendVerificationEmailTaskMixin


class ResendVerificationEmailTask(SendVerificationEmailTaskMixin, Task):

    email_sender = settings.ADMIN_SENDER_EMAIL
    email_subject = settings.REVERIFICATION_EMAIL_SUBJECT
    email_template = "emails/reverification_email.html"
