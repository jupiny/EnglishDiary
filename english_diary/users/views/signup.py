from django.views.generic.base import View
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "users/signup.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Validate username
        if get_user_model().objects.check_username(username):
            messages.add_message(
                request,
                messages.ERROR,
                settings.SIGNUP_NONVALIDATED_USERNAME_MESSAGE,
                extra_tags="danger",
            )
            return redirect(reverse("users:signup"))

        # Validate email
        if get_user_model().objects.check_email(email):
            messages.add_message(
                request,
                messages.ERROR,
                settings.SIGNUP_NONVALIDATED_EMAIL_MESSAGE,
                extra_tags="danger",
            )
            return redirect(reverse("users:signup"))

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        messages.add_message(
            request,
            messages.SUCCESS,
            settings.SIGNUP_SUCCESS_MESSAGE,
        )
        return redirect(reverse("users:signin"))
