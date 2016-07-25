from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib import messages


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
                "로그인이 성공적으로 되었습니다.",
            )
            return redirect(next_url)

        messages.add_message(
            request,
            messages.ERROR,
            "존재하지 않는 회원입니다.",
        )
        return redirect(reverse("users:signin"))
