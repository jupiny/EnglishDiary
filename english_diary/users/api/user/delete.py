import os
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserDeleteAPIView(APIView):

    def delete(self, request, *args, **kwargs):

        # Delete user's WordCloud image file
        if request.user.word_cloud:
            wordcloud_img_name = settings.IMAGE_FILENAME_FORMAT.format(
                username=request.user.username,
            )
            os.remove(os.path.join(settings.MEDIA_ROOT, wordcloud_img_name))

        # Delete user
        request.user.delete()
        return Response(
            status=status.HTTP_201_CREATED,
        )
