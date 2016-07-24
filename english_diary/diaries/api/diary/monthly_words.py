from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DiaryMontlyWordsAPIView(APIView):

    def get(self, request, *args, **kwargs):

        year = kwargs.get("year")
        month = kwargs.get("month")
        monthly_words = request.user.monthly_words(
            year=year,
            month=month,
        )
        monthly_words_count = request.user.monthly_words_count(
            year=year,
            month=month,
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "words": monthly_words,
                "count": monthly_words_count,
            },
        )
