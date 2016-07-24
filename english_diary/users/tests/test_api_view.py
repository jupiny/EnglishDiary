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

        test_username = "test_username"
        test_password = "test_password"
        test_email = "test@example.com"

        # Create a user
        self.user = get_user_model().objects.create_user(
            username=test_username,
            password=test_password,
            email=test_email,
        )

        # Login
        self.client = APIClient()
        self.client.login(
            username=test_username,
            password=test_password,
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
