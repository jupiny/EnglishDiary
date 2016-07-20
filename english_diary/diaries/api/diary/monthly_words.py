from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DiaryMontlyWordsAPIView(APIView):

    def get(self, request, *args, **kwargs):

        year = kwargs.get("year")
        month = kwargs.get("month")
        datetime = year+"/"+month+"/"
        diaries = request.user.diary_set.filter(datetime__contains=datetime)

        monthly_words = []
        for diary in diaries:
            monthly_words += diary.used_words
        monthly_words_count = len(set(monthly_words))

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "words": monthly_words,
                "count": monthly_words_count,
            },
        )
