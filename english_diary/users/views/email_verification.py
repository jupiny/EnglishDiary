from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import View


class EmailVerificationView(View):

    def get(self, request, *args, **kwargs):
        verification_key = kwargs.get("verification_key")

        return redirect(reverse("home"))
