from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings
from django.views.generic import View
import datetime

from users.models import Profile


class EmailVerificationView(View):

    def get(self, request, *args, **kwargs):
        verification_key = kwargs.get("verification_key")
        profile = get_object_or_404(Profile, verification_key=verification_key)
        user = profile.user

        # Check if user is verified
        if not user.is_verified:

            # Check if user verification_key expires
            if datetime.datetime.now() > profile.key_expires:
                return redirect(
                    reverse(
                        "users:key_expires",
                        kwargs={
                            "verification_key": verification_key,
                        }
                    )
                )

            # User email verification is completed
            user.is_verified = True
            user.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                settings.EMAIL_VERIFICATION_COMPLETE_MESSAGE,
            )
        return redirect(reverse("home"))
