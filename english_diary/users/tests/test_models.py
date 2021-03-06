from django.contrib.auth import get_user_model

from core.tests.base import BaseTestCase


class UserModelTestCase(BaseTestCase):

    def setUp(self):
        super(UserModelTestCase, self).setUp()

        # Create sample diaries
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

    def test_check_username_in_user_model(self):

        test_wrong_username = "test_wrong_username"

        self.assertTrue(
            get_user_model().objects.check_username(self.test_username),
        )

        self.assertFalse(
            get_user_model().objects.check_username(test_wrong_username),
        )

    def test_check_email_in_user_model(self):

        test_wrong_email = "wrong@example.com"

        self.assertTrue(
            get_user_model().objects.check_email(self.test_email),
        )
        self.assertFalse(
            get_user_model().objects.check_email(test_wrong_email),
        )

    def test_user_has_correct_monthly_words(self):
        test_july_words = [
            "today",
            "it",
            "was",
            "very",
            "hot",
            "i",
            "went",
            "to",
            "the",
            "concert",
            "and",
            "had",
            "dinner",
            "with",
            "my",
            "friends",
        ]

        test_august_words = [
            "i",
            "watched",
            "a",
            "action",
            "movie",
            "with",
            "my",
            "family",
            "it",
            "was",
            "so",
            "exciting",
            "i",
            "was",
            "so",
            "tired",
            "today",
            "don`t",
            "want",
            "to",
            "do",
            "no",
            "more",
            ]

        self.assertEqual(
            sorted(test_july_words),
            sorted(
                self.user.monthly_words(
                    year="2016",
                    month="07",
                ),
            ),
        )
        self.assertEqual(
            sorted(test_august_words),
            sorted(
                self.user.monthly_words(
                    year="2016",
                    month="08",
                ),
            ),
        )

    def test_user_has_correct_distinct_monthly_words_count(self):

        self.assertEqual(
            16,
            self.user.distinct_monthly_words_count(
                year="2016",
                month="07",
            ),
        )
        self.assertEqual(
            20,
            self.user.distinct_monthly_words_count(
                year="2016",
                month="08",
            ),
        )

    def test_user_has_correct_whole_used_words(self):
        test_whole_used_words = [
            "today",
            "it",
            "was",
            "very",
            "hot",
            "i",
            "went",
            "to",
            "the",
            "concert",
            "and",
            "had",
            "dinner",
            "with",
            "my",
            "friends",
            "i",
            "watched",
            "a",
            "action",
            "movie",
            "with",
            "my",
            "family",
            "it",
            "was",
            "so",
            "exciting",
            "i",
            "was",
            "so",
            "tired",
            "today",
            "don`t",
            "want",
            "to",
            "do",
            "no",
            "more",
            ]

        self.assertEqual(
            sorted(test_whole_used_words),
            sorted(self.user.whole_used_words),
        )

    def test_user_has_correct_distinct_whole_used_words_count(self):

        self.assertEqual(
            29,
            self.user.distinct_whole_used_words_count,
        )
