from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings 

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
            content="Today I am very happy!",
            datetime="2016/07/01",
        )

    def test_diary_model_should_have_correct_word_count(self):

        self.assertEqual(
            self.diary.word_count,
            5,
        )
