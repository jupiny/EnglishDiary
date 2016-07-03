from diaries.serializers import DiaryModelSerializer

from rest_framework.generics import RetrieveAPIView

from diaries.models import Diary


class DiaryDetailAPIView(RetrieveAPIView):
    
    queryset = Diary.objects.all()
    serializer_class = DiaryModelSerializer
    lookup_field = "datetime"
    lookup_url_kwarg = "datetime"
