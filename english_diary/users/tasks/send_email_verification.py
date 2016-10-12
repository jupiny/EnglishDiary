from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.conf import settings

from celery import Task

from core.utils.email import send_email


class SendEmailVerificationTask(Task):

    def run(self, user_id):
        user = get_user_model().objects.get(pk=user_id)

        # Send email to only user who has email except for TEST_EMAIL
        if user.email and user.email != settings.TEST_EMAIL:
            send_email(
                sender=settings.ADMIN_SENDER_EMAIL,
                receiver=user.email,
                subject=settings.EMAIL_VERIFICATION_SUBJECT.format(
                    username=user.username
                ),
                html=render_to_string(
                    "emails/email_verification.html",
                    context={
                        "username": user.username,
                        "verification_key": user.profile.verification_key,
                    },
                ),
            )
