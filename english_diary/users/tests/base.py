from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from english_diary.celery import app


class UserBaseTestCase(TestCase):

    def setUp(self):

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
