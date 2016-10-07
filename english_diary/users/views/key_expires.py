from django.shortcuts import render
from django.views.generic import View


class KeyExpiresView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "users/key_expires.html",
            context={},
        )
