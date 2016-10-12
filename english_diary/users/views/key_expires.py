from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View

import datetime

from users.models import Profile


class KeyExpiresView(View):

    def get(self, request, *args, **kwargs):
        verification_key = kwargs.get("verification_key")
        profile = get_object_or_404(Profile, verification_key=verification_key)
        user = profile.user

        # Check if user is verified or user verification_key expires
        if user.is_verified or datetime.datetime.now() <= profile.key_expires:
            return redirect(reverse("home"))

        return render(
            request,
            "users/key_expires.html",
            context={},
        )
