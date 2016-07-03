from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 

from diaries.models import Diary


class DiaryCreateAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        datetime = request.POST.get("datetime")
        content = request.POST.get("content")
        try:
            diary = Diary.objects.get(datetime=datetime)

            # Update Diary
            diary.datetime = datetime
            diary.content = content
            diary.save()

        except Diary.DoesNotExist:

            # Create Diary
            Diary.objects.create(
                user=request.user,
                datetime=datetime,
                content=content,
            )
        
        return Response(
            status=status.HTTP_201_CREATED,
            data={
            },
        )
