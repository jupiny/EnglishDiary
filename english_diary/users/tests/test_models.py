from django.contrib.auth import get_user_model

from .base import UserBaseTestCase


class UserModelTestCase(UserBaseTestCase):

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
