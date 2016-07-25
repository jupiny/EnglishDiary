from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model


class SigninView(View):

    def get(self, request, *args, **kwargs):

        # maintain signed user
        if request.user.is_authenticated():
            return redirect("home")

        return render(
            request,
            "users/signin.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next_url") or reverse("home")

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                settings.SIGNIN_SUCCESS_MESSAGE,
            )
            return redirect(next_url)

        if not get_user_model().objects.check_username(username):
            # Nonexistent User
            messages.add_message(
                request,
                messages.ERROR,
                settings.SIGNIN_NONEXISTENT_USERNAME_MESSAGE,
                extra_tags="danger",
            )

        # Wrong Password
        messages.add_message(
            request,
            messages.ERROR,
            settings.SIGNIN_WRONG_PASSWORD_MESSAGE,
            extra_tags="danger",
        )
        return redirect(reverse("users:signin"))
