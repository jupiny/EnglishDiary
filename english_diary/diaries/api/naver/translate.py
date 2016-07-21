import os

import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TranslateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        # translate.js 의 request 받기
        content = request.POST.get("content")

        # Create headers
        URL = "https://openapi.naver.com/v1/language/translate"
        headers = {
            "X-Naver-Client-Id": os.environ.get("X_Naver_Client_Id"),
            "X-Naver-Client-Secret": os.environ.get("X_Naver_Client_Secret"),
        }
        # Get diary content
        data = {
            "source": "en",
            "target": "ko",
            "text": content,
        }

        response = requests.post(
            URL,
            headers=headers,
            data=data,
        )
        translated_text = response.json().get("message").get("result").get("translatedText")
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "content": translated_text,
            },
        )
