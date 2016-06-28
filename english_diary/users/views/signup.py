from django.views.generic.base import View
from django.contrib.auth import get_user_model
from django.shortcuts import render


class SignupView(View):

    def get(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        hash_id = request.POST.get("hash_id")
        profile_image = request.POST.get("profile_image")

        return render(
            request,
            "users/signup.html",
            context={},
        )
