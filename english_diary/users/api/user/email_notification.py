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

    def patch(self, request, *args, **kwargs):

        email_notification = request.POST.get("email_notification")

        boolean_email_notification = False
        if email_notification == "on":
            boolean_email_notification = True

        request.user.email_notification = boolean_email_notification
        request.user.save()

        return Response(
            status=status.HTTP_201_CREATED,
        )
