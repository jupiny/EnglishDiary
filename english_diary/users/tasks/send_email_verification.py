from django.conf import settings

from celery import Task

from users.mixins import SendEmailVerificationTaskMixin


class SendEmailVerificationTask(SendEmailVerificationTaskMixin, Task):

    email_sender = settings.ADMIN_SENDER_EMAIL
    email_subject = settings.EMAIL_VERIFICATION_SUBJECT
    email_template = "emails/email_verification.html"
