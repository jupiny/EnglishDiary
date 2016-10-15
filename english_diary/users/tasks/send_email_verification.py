from django.conf import settings

from celery import Task

from users.mixins import SendVerificationEmailTaskMixin


class SendEmailVerificationTask(SendVerificationEmailTaskMixin, Task):

    email_sender = settings.ADMIN_SENDER_EMAIL
    email_subject = settings.VERIFICATION_EMAIL_SUBJECT
    email_template = "emails/email_verification.html"
