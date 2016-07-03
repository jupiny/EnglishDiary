from rest_framework.serializers import ModelSerializer

from diaries.models import Diary


class DiaryDetailSerializer(ModelSerializer):

    class Meta:
        model = Diary
        fields = [
            "content",
        ]
