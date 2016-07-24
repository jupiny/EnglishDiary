from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserDeleteAPIView(APIView):

    def delete(self, request, *args, **kwargs):
        request.user.delete()
        return Response(
            status=status.HTTP_201_CREATED,
        )
