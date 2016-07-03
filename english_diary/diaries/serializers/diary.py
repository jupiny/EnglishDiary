from rest_framework.serializers import ModelSerializer

from diaries.models import Diary


class DiaryModelSerializer(ModelSerializer):

    class Meta:
        model = Diary
        fields = [
            "content",
        ]
