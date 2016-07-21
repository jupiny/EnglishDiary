from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from english_diary.celery import app


class DiaryBaseTestCase(TestCase):

    def setUp(self):

        # Run celery task synchronous
        app.conf.update(CELERY_ALWAYS_EAGER=True)

        test_username = "test_username"
        test_password = "test_password"

        # Create a user
        self.user = get_user_model().objects.create_user(
            username=test_username,
            password=test_password,
        )

        # Login
        self.client = APIClient()
        self.client.login(
            username=test_username,
            password=test_password,
        )
