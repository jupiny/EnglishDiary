from core.tests.base import BaseTestCase


class DiaryModelTestCase(BaseTestCase):

    def test_diary_model_should_have_correct_used_words(self):

        # Create a diary
        self.diary = self.user.diary_set.create(
            content="Today I am very happy!",
            datetime="2016/07/01",
        )
        test_used_words = [
            "today",
            "i",
            "am",
            "very",
            "happy",
        ]

        self.assertEqual(
            len(self.diary.used_words),
            5,
        )
        self.assertEqual(
            sorted(test_used_words),
            sorted(self.diary.used_words),
        )

    def test_diary_model_should_have_correct_used_words_without_overlapping(self):

        # Create a diary which has overlapping words in content
        self.diary = self.user.diary_set.create(
            content="Today I am very happy! I am going to crazy",
            datetime="2016/07/01",
        )
        test_used_words = [
            "today",
            "i",
            "am",
            "very",
            "happy",
            "going",
            "to",
            "crazy"
        ]

        self.assertEqual(
            len(self.diary.used_words),
            8,
        )
        self.assertEqual(
            sorted(test_used_words),
            sorted(self.diary.used_words),
        )
