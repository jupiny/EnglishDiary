from django.views.generic import View
from django.shortcuts import render
import datetime


class HomeView(View):

    def get(self, request, *args, **kwargs):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return render(
            request,
            "home.html",
            context={
                "today": today,     
            },
        )
