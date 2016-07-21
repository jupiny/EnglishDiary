from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import pyperclip


class SetClipboardView(APIView):

    def post(self, request, *args, **kwargs):

        content = request.POST.get("content")
        pyperclip.copy(content)

        return Response(
            status=status.HTTP_201_CREATED,
            data={
            },
        )
