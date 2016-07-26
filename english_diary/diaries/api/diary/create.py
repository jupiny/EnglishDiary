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
            diary = request.user.diary_set.get_or_none(datetime=datetime)
            if diary:
                # Diary Update
                diary.datetime = datetime
                diary.content = content
                diary.save(update_fields=['content'])

            else:
                # Diary Create
                request.user.diary_set.create(
                    datetime=datetime,
                    content=content,
                )
            """
            request.user.diary_set.update_or_create(
                datetime=datetime,
                defaults={
                    "content": content,
                }
            )
            """
            result = True

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "result": result,
            },
        )
