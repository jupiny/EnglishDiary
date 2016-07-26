from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from rest_framework.test import APIClient

from english_diary.celery import app
from diaries.models import Diary
from diaries.signals.post_save import post_save_diary
from users.signals.post_save import post_save_user


class DiaryBaseTestCase(TestCase):

    def setUp(self):

        # Disable Signals
        post_save.disconnect(post_save_user, sender=get_user_model())
        post_save.disconnect(post_save_diary, sender=Diary)

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
