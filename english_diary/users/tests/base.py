from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from rest_framework.test import APIClient

from english_diary.celery import app
from users.signals.post_save import post_save_user
from diaries.signals.post_save import post_save_diary
from diaries.models import Diary


class UserBaseTestCase(TestCase):

    def setUp(self):

        # Disable Signals
        post_save.disconnect(post_save_user, sender=get_user_model())
        post_save.disconnect(post_save_diary, sender=Diary)

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

        # Create diaries
        self.user.diary_set.create(
            datetime="2016/07/02",
            content="Today it was very hot!",
        )
        self.user.diary_set.create(
            datetime="2016/07/15",
            content="I went to the concert. And I had dinner with my friends",
        )
        self.user.diary_set.create(
            datetime="2016/08/11",
            content="I watched a action movie with my family. It was so exciting.",
        )
        self.user.diary_set.create(
            datetime="2016/08/29",
            content="I was so tired today. I don`t want to do no more",
        )
