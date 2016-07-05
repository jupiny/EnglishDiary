from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from diaries.models import Diary


class DiaryDetailAPIView(APIView):

    def get(self, request, *args, **kwargs):

        year = kwargs.get("year")
        month = kwargs.get("month")
        day = kwargs.get("day")
        datetime = year + "/" + month + "/" + day
        diary = Diary.objects.get_or_none(datetime=datetime)

        if diary:
            # Diary is exist
            content = diary.content
        else:
            # Diary is not exist
            content = ""

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "content": content,
            },
        )
