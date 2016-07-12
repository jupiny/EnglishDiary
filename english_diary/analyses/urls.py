from django.conf.urls import url, include

from analyses.views import *


urlpatterns = [
    url(r'^analysis/$', AnalysisView.as_view(), name="analysis"),
]
