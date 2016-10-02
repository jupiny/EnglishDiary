from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings

from core.utils.email import send_email


class SendEmailTestCase(TestCase):

    """
    def test_send__email(self):
        response = send_email(
            sender="sender@example.com",
            receiver="receiver@example.com",
            subject="test_subject",
            text="test_text",
        )

        self.assertEqual(
            response.status_code,
            200,
        )
    """
