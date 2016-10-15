from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings

from rest_framework.test import APIClient

from english_diary.celery import app
from diaries.signals.post_save import post_save_diary
from diaries.models import Diary

TEST_USERNAME = "test_username"
TEST_PASSWORD = "test_password"
TEST_EMAIL = settings.TEST_EMAIL


class BaseTestCase(TestCase):

    def setUp(self):

        # Disable Signals
        post_save.disconnect(post_save_diary, sender=Diary)

        # Run celery task synchronous
        app.conf.update(CELERY_ALWAYS_EAGER=True)

        self.test_username = TEST_USERNAME
        self.test_password = TEST_PASSWORD
        self.test_email = TEST_EMAIL

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

    def tearDown(self):

        # Logout
        self.client.logout()
