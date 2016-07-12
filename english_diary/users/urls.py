from django.conf.urls import url, include

from users.views import *


urlpatterns = [
    url(r'^signin/$', SigninView.as_view(), name="signin"),
    url(r'^signout/$', SignoutView.as_view(), name="signout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^analysis/$', AnalysisView.as_view(), name="analysis"),
]
