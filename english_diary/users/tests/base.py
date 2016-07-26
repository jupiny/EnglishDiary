from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from rest_framework.test import APIClient

from english_diary.celery import app
from users.signals.post_save import post_save_user


class UserBaseTestCase(TestCase):

    def setUp(self):

        # Disable Signals
        post_save.disconnect(post_save_user, sender=get_user_model())

        # Run celery task synchronous
        app.conf.update(CELERY_ALWAYS_EAGER=True)

        self.test_username = "test_username"
        self.test_password = "test_password"
        self.test_email = "test@example.com"

        # Create a user
        self.user = get_user_model().objects.create_user(
            username=self.test_username,
            password=self.test_password,
            email=self.test_email,
        )

        # Login
        self.client = APIClient()
        self.client.login(
            username=self.test_username,
            password=self.test_password,
        )
