from .base import DiaryBaseTestCase


class DiaryModelTestCase(DiaryBaseTestCase):

    def test_diary_model_should_have_correct_word_count(self):

        # Create a diary
        self.diary = self.user.diary_set.create(
            content="Today I am very happy!",
            datetime="2016/07/01",
        )

        self.assertEqual(
            self.diary.word_count,
            5,
        )
