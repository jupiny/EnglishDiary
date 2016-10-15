from django.contrib.auth import get_user_model

from core.tests.base import BaseTestCase


class ProfileModelTestCase(BaseTestCase):

    def test_user_has_verification_key(self):
        self.assertTrue(
            self.user.profile.verification_key,
        )

        self.assertFalse(
            get_user_model().objects.last().profile.is_expired_key,
        )

        self.assertFalse(
            get_user_model().objects.last().is_verified,
        )
