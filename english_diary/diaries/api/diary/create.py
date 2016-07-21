from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re

from diaries.models import Diary


class DiaryCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        datetime = request.POST.get("datetime")
        content = request.POST.get("content")

        # Search Korean in text
        has_korean = re.search(
            r".*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*",
            content,
        )

        result = False
        if not has_korean:
            request.user.diary_set.update_or_create(
                datetime=datetime,
                defaults={
                    "content": content,
                }
            )
            result = True

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "result": result,
            },
        )
