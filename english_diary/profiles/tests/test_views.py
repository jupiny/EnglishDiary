from django.test import Client
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
import datetime

from core.tests.base import BaseTestCase
from profiles.utils import set_expiration_date


class ProfileViewTestCase(BaseTestCase):

    def setUp(self):
        super(ProfileViewTestCase, self).setUp()
        self.client = Client()

    def test_verify_user_verification_key(self):
        response = self.client.get(
            reverse(
                "profiles:verify_email",
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
        self.user.profile.key_expires = set_expiration_date(-1)
        self.user.profile.save()

        self.assertTrue(
            get_user_model().objects.last().profile.is_expired_key,
        )

        response = self.client.get(
            reverse(
                "profiles:verify_email",
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
            reverse(
                "profiles:key_expires",
                kwargs={
                    "verification_key": self.user.profile.verification_key,
                }
            ),
        )

    def test_renew_user_verification_key(self):

        # Make verification_key expire
        self.user.profile.key_expires = set_expiration_date(-1)
        self.user.profile.save()

        self.assertTrue(
            get_user_model().objects.last().profile.is_expired_key,
        )

        # Save previous user verification key
        prev_verification_key = self.user.profile.verification_key

        response = self.client.post(
            reverse(
                "profiles:renew_key",
            ),
            data={
                "verification_key": self.user.profile.verification_key,
            },
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

        self.assertFalse(
            get_user_model().objects.last().profile.is_expired_key,
        )

        self.assertNotEqual(
            prev_verification_key,
            get_user_model().objects.last().profile.verification_key,
        )
