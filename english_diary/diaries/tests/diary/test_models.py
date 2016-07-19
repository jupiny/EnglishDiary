from .base import DiaryBaseTestCase


class DiaryModelTestCase(DiaryBaseTestCase):

    def test_diary_model_should_have_correct_words_count(self):

        # Create a diary
        self.diary = self.user.diary_set.create(
            content="Today I am very happy!",
            datetime="2016/07/01",
        )

        self.assertEqual(
            self.diary.words_count,
            5,
        )

    def test_diary_model_should_count_words_without_overlapping(self):

        # Create a diary which has overlapping words in content
        self.diary = self.user.diary_set.create(
            content="Today I am very happy! I am going to crazy",
            datetime="2016/07/01",
        )

        self.assertEqual(
            self.diary.words_count,
            8,
        )
