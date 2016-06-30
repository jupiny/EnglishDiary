from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime

from diaries.models import Diary


class DiaryModelTestCase(TestCase):

    def setUp(self):

        # Create a user
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
        )

        # Create a diary
        self.diary = self.user.diary_set.create(
            content="content",
        )
        self.diary.created_at = datetime(2016, 6, 30, 15, 18, 38)

    def test_diary_model_should_have_formatted_created_at(self):

        self.assertEqual(
            self.diary.formatted_created_at,
            '2016-06-30',
        )
