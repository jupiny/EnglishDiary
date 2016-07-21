from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class DictionaryTestCase(APITestCase):

    def test_dictionary_api_should_return_english_word_form_korean_word(self):

        test_korean_word = "사과"
        test_dictionary_url = reverse(
            'api:naver:dict',
            kwargs={
                "find_word": test_korean_word,
            }
        )
        response = self.client.get(
            test_dictionary_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertIn(
            "apple",
            response.data.get("word_meaning"),
        )

    def test_dictionary_api_should_return_korean_word_form_english_word(self):

        test_english_word = "apple"
        test_dictionary_url = reverse(
            'api:naver:dict',
            kwargs={
                "find_word": test_english_word,
            }
        )
        response = self.client.get(
            test_dictionary_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertIn(
            "사과",
            response.data.get("word_meaning"),
        )

    def test_dictionary_api_should_return_nothing_when_nonexistent_korean_word(self):

        test_nonexistent_korean_word = "아갸야라"
        test_dictionary_url = reverse(
            "api:naver:dict",
            kwargs={
                "find_word": test_nonexistent_korean_word,
            }
        )
        response = self.client.get(
            test_dictionary_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertFalse(
            response.data.get("word_meaning"),
        )

    def test_dictionary_api_should_return_nothing_when_nonexistent_english_word(self):

        test_nonexistent_english_word = "asfasdfasdf"
        test_dictionary_url = reverse(
            "api:naver:dict",
            kwargs={
                "find_word": test_nonexistent_english_word,
            }
        )
        response = self.client.get(
            test_dictionary_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertFalse(
            response.data.get("word_meaning"),
        )
