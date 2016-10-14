from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from core.utils.email import send_email


class SendEmailVerificationTaskMixin(object):

    @property
    def email_sender(self):
        return NotImplemented

    @property
    def email_subject(self):
        return NotImplemented

    @property
    def email_template(self):
        return NotImplemented

    def run(self, user_id):
        user = get_user_model().objects.get(pk=user_id)

        # Send email to only user who has email except for TEST_EMAIL
        if user.email and user.email != settings.TEST_EMAIL:
            send_email(
                sender=self.email_sender,
                receiver=user.email,
                subject=self.email_subject.format(
                    username=user.username
                ),
                html=render_to_string(
                    self.email_template,
                    context={
                        "username": user.username,
                        "verification_key": user.profile.verification_key,
                    },
                ),
            )
