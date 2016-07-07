import os
import requests
import json

from django.test import TestCase


class TranslateTestCase(TestCase):

    def setUp(self):

        # Create headers
        URL = "https://openapi.naver.com/v1/language/translate"

        headers = {
            "X-Naver-Client-Id": os.environ.get("X_Naver_Client_Id"),
            "X-Naver-Client-Secret": os.environ.get("X_Naver_Client_Secret"),
        }
        data = {
            "source": "en",
            "target": "ko",
            "text": "Hi, This is test.",
        }

        self.response = requests.post(
            URL,
            headers=headers,
            data=data,
        )

    def test_naver_translate_API_should_return_200(self):
        self.assertEqual(
            self.response.status_code,
            200,
        )

    def test_naver_translate_API_should_have_text(self):

        self.assertEqual(
            self.response.json().get("message").get("result").get("translatedText"),
            "안녕, 이것은 시험."
        )
