from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from english_diary.celery import app


class UserAPIViewTestCase(TestCase):

    def setUp(self):

        # Run celery task synchronous
        app.conf.update(CELERY_ALWAYS_EAGER=True)

        self.test_username = "test_username"
        self.test_password = "test_password"
        self.test_email = "test@example.com"

        # Create a user
        self.user = get_user_model().objects.create_user(
            username=self.test_username,
            password=self.test_password,
            email=self.test_email,
        )

        # Login
        self.client = APIClient()
        self.client.login(
            username=self.test_username,
            password=self.test_password,
        )

    def test_user_change_email(self):

        test_user_email_url = reverse('api:user:email')
        test_new_email = "new@example.com"

        test_data = {
            'new_email': test_new_email,
        }

        response = self.client.patch(
            test_user_email_url,
            test_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            get_user_model().objects.last().email,
            test_new_email,
        )

    def test_user_change_password(self):

        test_user_password_url = reverse('api:user:password')
        test_new_password = "test_new_password"

        test_data = {
            'current_password': self.test_password,
            'new_password': test_new_password,
            'confirm_new_password': test_new_password,
        }

        response = self.client.patch(
            test_user_password_url,
            test_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertTrue(
            response.data.get("is_current_password_valid"),
        )
        self.assertTrue(
            response.data.get("does_match_confirm_password"),
        )
        self.assertTrue(
            get_user_model().objects.last().check_password(test_new_password),
        )

    def test_user_enter_wrong_current_password(self):

        test_user_password_url = reverse('api:user:password')
        test_wrong_password = "test_wrong_password"
        test_new_password = "test_new_password"

        test_data = {
            'current_password': test_wrong_password,
            'new_password': test_new_password,
            'confirm_new_password': test_new_password,
        }

        response = self.client.patch(
            test_user_password_url,
            test_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertFalse(
            response.data.get("is_current_password_valid"),
        )
        self.assertTrue(
            response.data.get("does_match_confirm_password"),
        )
        self.assertFalse(
            get_user_model().objects.last().check_password(test_new_password),
        )

    def test_new_password_does_not_match_cofirmation(self):

        test_user_password_url = reverse('api:user:password')
        test_new_password = "test_new_password"

        test_data = {
            'current_password': self.test_password,
            'new_password': test_new_password,
            'confirm_new_password': test_new_password+"!",
        }

        response = self.client.patch(
            test_user_password_url,
            test_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertTrue(
            response.data.get("is_current_password_valid"),
        )
        self.assertFalse(
            response.data.get("does_match_confirm_password"),
        )
        self.assertFalse(
            get_user_model().objects.last().check_password(test_new_password),
        )

    def test_user_enter_wrong_current_password_and_new_password_does_not_match_cofirmation(self):

        test_user_password_url = reverse('api:user:password')
        test_wrong_password = "test_wrong_password"
        test_new_password = "test_new_password"

        test_data = {
            'current_password': test_wrong_password,
            'new_password': test_new_password,
            'confirm_new_password': test_new_password+"!",
        }

        response = self.client.patch(
            test_user_password_url,
            test_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertFalse(
            response.data.get("is_current_password_valid"),
        )
        self.assertFalse(
            response.data.get("does_match_confirm_password"),
        )
        self.assertFalse(
            get_user_model().objects.last().check_password(test_new_password),
        )

    def test_get_default_email_notification(self):

        test_user_email_notification_url = reverse(
            'api:user:email_notification',
        )

        response = self.client.get(
            test_user_email_notification_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertTrue(
            response.data.get("email_notification"),
        )

    def test_get_changed_email_notification(self):

        test_user_email_notification_url = reverse(
            'api:user:email_notification',
        )

        self.user.email_notification = False
        self.user.save()

        response = self.client.get(
            test_user_email_notification_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertFalse(
            response.data.get("email_notification"),
        )

    def test_user_set_email_notification_true(self):

        test_user_email_noficatoin_url = reverse('api:user:email_notification')

        self.user.email_notification = True
        self.user.save()

        test_data = {
            'email_notification': 'off',
        }

        response = self.client.patch(
            test_user_email_noficatoin_url,
            test_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertFalse(
            get_user_model().objects.last().email_notification,
        )

    def test_user_set_email_notification_false(self):

        test_user_email_noficatoin_url = reverse('api:user:email_notification')

        self.user.email_notification = False
        self.user.save()

        test_data = {
            'email_notification': 'on',
        }

        response = self.client.patch(
            test_user_email_noficatoin_url,
            test_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertTrue(
            get_user_model().objects.last().email_notification,
        )

    def test_delete_user(self):

        test_user_delete_url = reverse('api:user:delete')

        response = self.client.delete(
            test_user_delete_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            get_user_model().objects.count(),
            0,
        )
