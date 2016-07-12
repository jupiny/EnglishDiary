from django.views.generic.base import View
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


class AnalysisView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "users/analysis.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        return redirect(reverse("users:analysis"))
