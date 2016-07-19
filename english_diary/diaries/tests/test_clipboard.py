from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
import pyperclip


class ClipboardTestCase(TestCase):

    def test_copy_content_to_clipboard(self):

        test_clipboard_url = reverse('api:clipboard')
        test_content = "I want to copy this content"

        test_data = {
            'content': test_content,
        }

        response = self.client.post(
            test_clipboard_url,
            test_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            pyperclip.paste(),
            test_content,
        )
