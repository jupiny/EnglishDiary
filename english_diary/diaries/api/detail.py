from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 

from diaries.models import Diary


class DiaryDetailAPIView(APIView):

    def get(self, request, *args, **kwargs):

        try:
            diary = Diary.objects.get(datetime=kwargs.get("datetime"))

            # Diary is exist
            content = diary.content

        except Diary.DoesNotExist:

            #Diary is not exist
            content = ""

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "content": content,
            },
        )
