

from rest_framework.generics import RetrieveAPIView

from diaries.serializers import DiaryDetailSerializer
from diaries.models import Diary


class DiaryDetailAPIView(RetrieveAPIView):
    
    queryset = Diary.objects.all()
    serializer_class = DiaryDetailSerializer
    lookup_field = "formatted_created_at"
    lookup_url_kwarg = "datetime"
