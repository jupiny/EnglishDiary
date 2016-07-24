from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserPasswordAPIView(APIView):

    def patch(self, request, *args, **kwargs):
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_new_password = request.POST.get("confirm_new_password")
        username = request.user.username

        is_current_password_valid = False
        does_match_confirm_password = False

        if request.user.check_password(current_password):
            is_current_password_valid = True

        if new_password == confirm_new_password:
            does_match_confirm_password = True

        if is_current_password_valid and does_match_confirm_password:

            # Change password
            request.user.set_password(new_password)
            request.user.save()

            # Log in with new password
            user = authenticate(
                username=username,
                password=new_password,
            )
            login(request, user)

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "is_current_password_valid": is_current_password_valid,
                "does_match_confirm_password": does_match_confirm_password,
            }
        )
