from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import Client
from django.conf import settings
import datetime

from .base import UserBaseTestCase


class UserVerifyEmaillTestCase(UserBaseTestCase):

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

    def test_verify_user_verification_key(self):
        client = Client()
        response = client.get(
            reverse(
                "users:email_verification",
                kwargs={
                    "verification_key": self.user.profile.verification_key,
                }
            ),
            follow=True,
        )

        self.assertEqual(
           response.status_code,
           200,
        )

        self.assertRedirects(
            response,
            "/signin/?next=/",
        )

        self.assertTrue(
            get_user_model().objects.last().is_verified,
        )

    def test_user_verification_key_expires(self):

        # Make verification_key expire
        self.user.profile.key_expires = datetime.datetime.strftime(
            datetime.datetime.now()-datetime.timedelta(days=settings.KEY_EXPIRES_DAY+1),
            "%Y-%m-%d %H:%M:%S",
        )
        self.user.profile.save()

        client = Client()
        response = client.get(
            reverse(
                "users:email_verification",
                kwargs={
                    "verification_key": self.user.profile.verification_key,
                }
            ),
            follow=True,
        )

        self.assertTrue(
            get_user_model().objects.last().profile.is_expired_key,
        )

        self.assertEqual(
           response.status_code,
           200,
        )

        self.assertRedirects(
            response,
            reverse(
                "users:key_expires",
                kwargs={
                    "verification_key": self.user.profile.verification_key,
                }
            ),
        )
