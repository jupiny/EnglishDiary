from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserEmailNotificationAPIView(APIView):

    def get(self, request, *args, **kwargs):

        email_notification = request.user.email_notification

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "email_notification": email_notification,
            }
        )
