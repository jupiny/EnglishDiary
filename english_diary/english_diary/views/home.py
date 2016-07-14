from django.views.generic import View
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        today = datetime.now().strftime("%Y-%m-%d")
        return render(
            request,
            "home.html",
            context={
                "today": today,
            },
        )
