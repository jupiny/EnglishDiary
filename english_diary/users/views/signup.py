from django.views.generic.base import View
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


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

        # TODO: validation with test code
        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            email=email,
        )

        # TODO: flash message(success, error)
        return redirect(reverse("users:login"))
