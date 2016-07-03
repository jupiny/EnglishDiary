from django.contrib.auth import logout
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class SignoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("users:signin"))
