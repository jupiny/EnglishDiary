from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View


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

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return redirect("home")

        return redirect(reverse("users:signin"))
