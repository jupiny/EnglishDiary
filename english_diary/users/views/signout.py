from django.contrib.auth import logout
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings


class SignoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            settings.SIGNOUT_SUCCESS_MESSAGE,
        )
        return redirect(reverse("users:signin"))
