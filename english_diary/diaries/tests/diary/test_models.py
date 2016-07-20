from .base import DiaryBaseTestCase


class DiaryModelTestCase(DiaryBaseTestCase):

    def test_diary_model_should_have_correct_used_words(self):

        # Create a diary
        self.diary = self.user.diary_set.create(
            content="Today I am very happy!",
            datetime="2016/07/01",
        )

        self.assertEqual(
            len(self.diary.used_words),
            5,
        )
        self.assertEqual(
            ["Today", "I", "am", "very", "happy"].sort(),
            self.diary.used_words.sort(),
        )

    def test_diary_model_should_have_correct_used_words_without_overlapping(self):

        # Create a diary which has overlapping words in content
        self.diary = self.user.diary_set.create(
            content="Today I am very happy! I am going to crazy",
            datetime="2016/07/01",
        )

        self.assertEqual(
            len(self.diary.used_words),
            8,
        )
        self.assertEqual(
            ["Today", "I", "am", "very", "happy", "going", "to", "crazy"].sort(),
            self.diary.used_words.sort(),
        )
