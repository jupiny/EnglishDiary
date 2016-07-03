from diaries.serializers import DiaryDetailSerializer
from django.shortcuts import get_object_or_404

from rest_framework.generics import RetrieveAPIView

from diaries.models import Diary


class DiaryDetailAPIView(RetrieveAPIView):
    
    queryset = Diary.objects.all()
    serializer_class = DiaryDetailSerializer
    lookup_field = "formatted_created_at"
    lookup_url_kwarg = "datetime"
