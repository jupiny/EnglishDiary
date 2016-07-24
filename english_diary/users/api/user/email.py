from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model


class UserEmailAPIView(APIView):

    def patch(self, request, *args, **kwargs):
        new_email = request.POST.get("new_email")
        request.user.email = new_email
        request.user.save()

        return Response(
            status=status.HTTP_201_CREATED,
        )
