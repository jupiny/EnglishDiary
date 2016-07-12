from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings

from diaries.models import Diary


class AnalysisTestCase(TestCase):

    def setUp(self):

        # Create a user
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
        )

        # Create first diary
        self.diary_1 = self.user.diary_set.create(
            content="Today I am very happy",
            datetime="2016/07/01",
        )
        # Create second diary
        self.diary_2 = self.user.diary_set.create(
            content="Today I am very happy again",
            datetime="2016/07/02",
        )

        # compare diaries
        self.new_word = set(self.diary_2.content.split()) - set(self.diary_1.content.split())

        # TODO: 특수문자 제거처리 (정규표현식?!)

    def test_new_word_should_have_correct_word_count(self):

        self.assertEqual(
            self.new_word,
            {"again"},
        )
